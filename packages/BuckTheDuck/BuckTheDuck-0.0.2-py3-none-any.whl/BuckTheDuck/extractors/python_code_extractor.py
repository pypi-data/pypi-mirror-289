import ast
import re
from typing import List, Tuple

from unidiff import PatchSet, PatchedFile, Hunk

from BuckTheDuck import get_logger
from BuckTheDuck.extractors.base_extractor import BaseExtractor
from BuckTheDuck.extractors.types.extracted_commit_changes import ExtractedCommitChanges, ChangeMapping, MethodMapping, \
    MethodStatus
from BuckTheDuck.extractors.types.supported_languages import SupportedLanguages

logger = get_logger()


class PythonCodeExtractor(BaseExtractor):
    _REGEX_FOR_METHOD_NAME = r"^\s*def\s+(\w+)\s*\(.*\)\s*(->\s*[\w\[\], ]+)?\s*:"
    _LOG_PREFIX = 'PythonCodeExtractor'

    def extract_from_commits(self, patch_set: PatchSet, extracted_commit_changes: ExtractedCommitChanges):
        logger.info(f'{self._LOG_PREFIX}: Starting to extract from commit')
        for file in patch_set:
            if not file.path.endswith(SupportedLanguages.PYTHON.value):
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

    def _extract_class_name_from_deleted_file(self, file: PatchedFile) -> str:
        return ''

    def _extract_changes(self, file: PatchedFile) -> List[ChangeMapping]:
        with open(file.path, "r") as file_opened:
            file_content = file_opened.read()

        # Parse the file content into an AST
        tree = ast.parse(file_content)

        change_mappings = []
        # Traverse the AST to find class definitions
        for node in ast.walk(tree):
            methods = []
            if isinstance(node, ast.ClassDef):
                class_name = node.name

                if file.is_modified_file:
                    original_methods_names = [n.name for n in node.body if
                                     isinstance(n, ast.FunctionDef)]
                    methods_scope = [(n.name, n.lineno, n.end_lineno) for n in node.body if
                                     isinstance(n, ast.FunctionDef)]
                    unseen_method_names = original_methods_names.copy()
                    for file_hunk in file:
                        methods.extend(self._get_method_name(unseen_method_names, file_hunk))

                    if unseen_method_names:
                        self._detect_edited_methods(file, methods, methods_scope)
                else:
                    methods = [MethodMapping(n.name, MethodStatus.ADDED) for n in node.body if
                               isinstance(n, ast.FunctionDef)]

                if methods:
                    change_mapping = ChangeMapping(class_name, methods)
                    change_mappings.append(change_mapping)

        return change_mappings

    def _get_method_name(self, methods_names: List[str], file_changes_hunk: Hunk):
        methods = []
        for line_change in file_changes_hunk:
            self._detect_created_method_from_line(line_change, methods_names, methods)

        return methods

    def _detect_edited_methods(self, file, methods, methods_scope):
        seen_methods = [method.method_name for method in methods]
        for (method_name, method_line_start, method_line_end) in methods_scope:
            for file_changes_hunk in file:
                method_modified = False
                for line_change in file_changes_hunk:
                    if line_change.target_line_no is None:
                        logger.info(f'{self._LOG_PREFIX}: {line_change=} line number is None, continuing')
                        continue
                    if (method_name not in seen_methods and
                            method_line_start < line_change.target_line_no < method_line_end):
                        method_modified = True
                        seen_methods.append(method_name)
                        break
                if method_modified:
                    methods.append(MethodMapping(method_name, MethodStatus.EDITED))

    def _detect_created_method_from_line(self, line_change, methods_names, methods):
        if 'def ' in line_change.value:
            if line_change.is_context:
                return
            method_name = self._get_method_name_from_line(line_change, self._REGEX_FOR_METHOD_NAME)
            if not method_name:
                return
            if method_name in methods_names:
                methods_names.remove(method_name)
                if line_change.is_removed:
                    pass
                elif line_change.is_added:
                    methods.append(MethodMapping(method_name, MethodStatus.ADDED))

    def _get_method_name_from_line(self, line_change, regex_for_method_name):
        match = re.search(regex_for_method_name, line_change.value)
        method_name = None
        if match:
            method_name = match.group(1)
        return method_name

