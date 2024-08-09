import re
from typing import List, Tuple
from BuckTheDuck import get_logger
from BuckTheDuck.documentor.file_documentor.language_parser.base_language_parser import BaseLanguageParser
from BuckTheDuck.documentor.file_mapping import FileMapping, Method

logger = get_logger()


class PythonParser(BaseLanguageParser):
    LOG_PREFIX = 'PythonParser'

    def __init__(self):
        self._init_method_attributes()

    def _init_method_attributes(self):
        self.__method_name = None
        self.__arguments = None
        self.__return_type = None
        self.__start_line = None
        self.__end_line = None
        self.__method_content = ''

    def parse_file(self, file) -> FileMapping:
        with open(file, 'r') as code_file:
            class_name = ''
            public_methods: List[Method] = []
            private_methods: List[Method] = []
            for line_number, line in enumerate(code_file.readlines()):
                if self.__method_name and not line.lstrip().startswith('def '):
                    self.__method_content += line
                if self.__method_name and not self.__start_line:
                    self.__start_line = line_number
                elif line.lower().startswith('class'):
                    class_name = self._get_class_name(line)
                    logger.info(f'{self.LOG_PREFIX}: Class detected {class_name=}')
                    continue
                elif line.lstrip().startswith('def '):
                    if self.__method_name:
                        logger.info(f'{self.LOG_PREFIX}: Closing existing open method {self.__method_name} '
                                    'before opening the next')
                        method = self._create_method(line_number)
                        if self._is_public_method(self.__method_name):
                            public_methods.append(method)
                        else:
                            private_methods.append(method)
                    self._init_method_attributes()
                    self.__method_name = self._get_method_name(line)
                    self.__arguments = self._get_method_arguments(line)
                    self.__return_type = self._get_method_return_type(line)
                    self.__method_content += line
                    logger.info(f'{self.LOG_PREFIX}: New method detected {self.__method_name=}, '
                                f'{self.__arguments=}, {self.__return_type=}')

            return FileMapping(class_name, public_methods, private_methods)

    def _get_class_name(self, line) -> str:
        pattern = r'^class\s+(\w+)\s*(\(.*\))?:'
        match = re.match(pattern, line)
        if match:
            return match.group(1)
        return ''

    def _get_method_name(self, line) -> str:
        pattern = r'^def\s+(\w+)\s*\(([^)]*)\)\s*(->\s*\w+\s*)?:\s*'
        match = re.match(pattern, line.lstrip())
        if match:
            return match.group(1)
        return ''

    def _get_method_arguments(self, line) -> List[str]:
        pattern = r'^def\s+(\w+)\s*\(([^)]*)\)\s*(->\s*\w+\s*)?:\s*'
        match = re.match(pattern, line.lstrip())
        if match:
            arguments_str = match.group(2)
            arguments = arguments_str.split(',')
            arguments = [s.strip() for s in arguments]
            try:
                arguments.remove('self')
            except:
                pass
            return arguments
        return []

    def _get_method_return_type(self, line):
        pattern = r'^def\s+(\w+)\s*\(([^)]*)\)\s*(->\s*\w+\s*)?:\s*'
        match = re.match(pattern, line.lstrip())
        if match:
            return_type = match.group(3)
            if return_type:
                return_type = return_type.replace('-> ', '')
            return return_type
        return []

    def _get_method_boundaries(self, line_number_from_upper_scope, code_file) -> Tuple[int, int]:
        pass

    def _is_public_method(self, method_name) -> bool:
        return not method_name.startswith('_')

    def _create_method(self, line_number):
        end_line = line_number
        logger.info(f'{self.LOG_PREFIX}: Method detected {self.__method_name=} {self.__start_line=} {self.__end_line=}')
        method = Method(self.__method_name, self.__arguments, self.__return_type, self.__start_line, end_line,
                        self.__method_content)
        return method
