import os
from typing import List

from BuckTheDuck import get_logger
from BuckTheDuck.documentor.file_documentor.file_documentor import FileDocumentor

logger = get_logger()


class DocumentationManager:
    _LOGGER_PREFIX = 'DocumentationManager'
    _DOCUMENTATION_REPO = '.buck'

    def __init__(self):
        self._current_working_directory = os.getcwd()
        self._init_repo()
        self._file_documentor = FileDocumentor()

    def document_project(self, path: str):
        self._iterate_directory(path)

    def update_documentation(self, files: List[str]):
        for file in files:
            self._document_file(file)

    def _iterate_directory(self, directory):
        if self._is_python_module(directory):
            logger.info(f"{self._LOGGER_PREFIX}: '{directory}' is a Python module.")

            for entry in os.listdir(directory):
                entry_path = os.path.join(directory, entry)
                if '__init__.py' == entry:
                    continue
                if os.path.isdir(entry_path):
                    self._iterate_directory(entry_path)
                elif entry.endswith('.py'):
                    logger.info(f"{self._LOGGER_PREFIX}: Python file found: {entry_path}")
                    self._document_file(entry_path, entry)
        else:
            logger.info(f"{self._LOGGER_PREFIX}: '{directory}' is not a Python module. Skipping subdirectories.")

    def _is_python_module(self, directory):
        return os.path.isfile(os.path.join(directory, '__init__.py'))

    def _document_file(self, entry_path, entry, create_file=True):
        try:
            doc_file_name = entry.replace('.py', '.md')
            doc_file_path = os.path.join(self._current_working_directory, self._DOCUMENTATION_REPO, doc_file_name)
            if create_file and os.path.isfile(doc_file_path):
                logger.info(f'{self._LOGGER_PREFIX}: Skipping file {entry} as we already have documentation')
                return
            markdown_text = self._file_documentor.document_file(entry_path)
            if not markdown_text:
                logger.warning(f'{self._LOGGER_PREFIX}: Skipping file {entry} as not markdown generated')
                return
            with open(doc_file_path, 'w') as doc_file:
                doc_file.writelines(markdown_text)
        except Exception as e:
            logger.exception(f'{self._LOGGER_PREFIX}: Failed to generate doc for a file {entry_path}, due to error {e} '
                             '- continuing to the next file')

    def _init_repo(self):
        dest_path = os.path.join(self._current_working_directory, self._DOCUMENTATION_REPO)
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)
