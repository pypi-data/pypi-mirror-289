from BuckTheDuck import get_logger
from BuckTheDuck.documentor.file_documentor.language_parser.python_parser import PythonParser
from BuckTheDuck.documentor.file_mapping import FileMapping

from BuckTheDuck.generative_ai.summarize_file_generator import SummarizeFileGenerator

logger = get_logger()


class FileDocumentor:
    def __init__(self):
        self._summarize_file_generator = SummarizeFileGenerator()

    def document_file(self, file):
        file_mapping = self._map_file(file)
        markdown_text = self._summarize_file_generator.generate_markdown(file_mapping)
        return markdown_text


    def _map_file(self, file) -> FileMapping:
        return PythonParser().parse_file(file)
