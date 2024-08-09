import re
from typing import List

import py_mini_racer
from unidiff import PatchSet, PatchedFile

from BuckTheDuck import get_logger
from BuckTheDuck.common.file_path_utilities import FilePathUtilities
from BuckTheDuck.extractors.ast_parser.nodejs_ast_parser import NodejsAstParser
from BuckTheDuck.extractors.base_extractor import BaseExtractor
from BuckTheDuck.extractors.types.extracted_commit_changes import ExtractedCommitChanges, ChangeMapping, MethodMapping, \
    MethodStatus, ClassProperties
from BuckTheDuck.extractors.types.supported_languages import SupportedLanguages

logger = get_logger()


class NodeJsExtractor(BaseExtractor):
    _LOG_PREFIX = 'NodeJsExtractor'

    def __init__(self):
        with open('babel-parser/dist/bundle.js', 'r') as file:
            bundled_code = file.read()

        self.js_context = py_mini_racer.MiniRacer()
        self.js_context.eval(bundled_code)
        self._ast_node_parser = NodejsAstParser()

    def extract_from_commits(self, patch_set: PatchSet, extracted_commit_changes: ExtractedCommitChanges):
        for file in patch_set:
            file_extension = FilePathUtilities.extract_file_extension(file.path)
            if not file_extension or file_extension not in SupportedLanguages.nodejs_files():
                continue
            if file.is_removed_file:
                class_name = self._extract_class_name_from_deleted_file(file)
                extracted_commit_changes.add_removed_class([class_name])
            else:
                change_mappings = self._extract_changes(file)
                if file.is_added_file:
                    extracted_commit_changes.add_new_changes(change_mappings)
                elif file.is_modified_file:
                    extracted_commit_changes.add_changes(change_mappings)

    def _extract_changes(self, file: PatchedFile) -> List[ChangeMapping]:
        with open(file.path, "r") as file_opened:
            file_content = file_opened.read()

        ast = self.js_context.call("parseTypeScript", file_content)

        parsed_ast = self._ast_node_parser.parse(ast)
        change_mappings = []
        for ast in parsed_ast:
            if file.is_modified_file:
                unseen_method_names = [method.name for method in ast.methods]
                methods = []
                change_mapping = ChangeMapping(
                    class_name=ast.class_name,
                    method_name=[],
                    properties=[ClassProperties(single_property.name, single_property.ts_type)
                                for single_property in ast.properties])
                self._add_new_methods(change_mapping, file, methods, unseen_method_names)
                self._add_edited_methods(ast, change_mapping, file, unseen_method_names)
                change_mappings.append(change_mapping)
            elif file.is_added_file:
                change_mapping = ChangeMapping(
                    class_name=ast.class_name,
                    method_name=[MethodMapping(method.name, MethodStatus.ADDED) for method in ast.methods],
                    properties=[ClassProperties(single_property.name, single_property.ts_type) for single_property in
                                ast.properties]
                )
                change_mappings.append(change_mapping)

        return change_mappings

    def _add_new_methods(self, change_mapping, file, methods, unseen_method_names):
        for file_hunk in file:
            methods.extend(self._detect_new_methods(file_hunk, unseen_method_names))
        for method in methods:
            change_mapping.method_name.append(MethodMapping(method, MethodStatus.ADDED))

    def _add_edited_methods(self, ast, change_mapping, file, unseen_method_names):
        if unseen_method_names:
            edited_methods = self._detect_edited_methods(file, ast.methods, unseen_method_names)
            if edited_methods:
                for edited_method in edited_methods:
                    change_mapping.method_name.append(MethodMapping(edited_method, MethodStatus.EDITED))

    def _extract_class_name_from_deleted_file(self, file: PatchedFile) -> str:
        return ''

    def _extract_file_extension(self, path):
        pattern = r"\.([a-zA-Z0-9]+)$"
        match = re.search(pattern, path)
        if match:
            file_extension = match.group(1)
            return file_extension

    def _detect_new_methods(self, file_hunk, unseen_method_names):
        pattern_combined = (
            r'\s*function\s+(?P<name>\w+)\s*\([^)]*\)\s*(?::\s*\w+)?\s*{[^}]*}'  # Function declarations
            r'|\s*(?P<name_arrow>\w+)\s*=\s*\([^)]*\)\s*(?::\s*\w+)?\s*=>\s*{[^}]*}'  # Arrow functions
            r'|\s*class\s+(?P<class_name>\w+)\s*{[^}]*}'  # Class definitions
            r'|\s*(?P<method_name>\w+)\s*\([^)]*\)\s*(?::\s*\w+)?\s*{'  # Class methods
        )
        new_methods = []
        for line_change in file_hunk:
            if line_change.is_context or line_change.is_removed:
                continue
            matches = re.match(pattern_combined, line_change.value)
            if not matches:
                continue
            for match in matches.groups():
                if match:
                    new_methods.append(match)
                    unseen_method_names.remove(match)

        return new_methods

    def _detect_edited_methods(self, file, methods, unseen_method_names):
        seen_methods = [method.name for method in methods if method.name in unseen_method_names]
        edited_methods = []
        for method in methods:
            if method.name not in seen_methods:
                continue
            for file_hunk in file:
                method_modified = False
                for line_change in file_hunk:
                    if line_change.target_line_no is None:
                        logger.info(f'{self._LOG_PREFIX}: {line_change=} line number is None, continuing')
                        continue
                    if method.start_line < line_change.target_line_no < method.end_line:
                        method_modified = True
                        break
                if method_modified:
                    edited_methods.append(MethodMapping(method.name, MethodStatus.EDITED))

        return edited_methods
