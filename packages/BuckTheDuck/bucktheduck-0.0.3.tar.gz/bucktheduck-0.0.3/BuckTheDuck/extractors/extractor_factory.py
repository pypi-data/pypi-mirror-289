from BuckTheDuck.common.exceptions import UnsupportedOperation
from BuckTheDuck.extractors.nodejs_extractor import NodeJsExtractor
from BuckTheDuck.extractors.python_code_extractor import PythonCodeExtractor
from BuckTheDuck.extractors.types.supported_languages import SupportedLanguages


class ExtractorFactory:

    def create(self, project_language: SupportedLanguages):
        if project_language == SupportedLanguages.PYTHON:
            return PythonCodeExtractor()
        elif project_language in [SupportedLanguages.JAVASCRIPT, SupportedLanguages.JAVASCRIPT_X,
                                  SupportedLanguages.TYPESCRIPT, SupportedLanguages.TYPESCRIPT_X]:
            return NodeJsExtractor()
        else:
            raise UnsupportedOperation('Language not supported yet')