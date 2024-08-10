from enum import Enum


class SupportedLanguages(Enum):
    PYTHON = 'py'
    TYPESCRIPT = 'ts'
    TYPESCRIPT_X = 'tsx'
    JAVASCRIPT = 'js'
    JAVASCRIPT_X = 'jsx'

    @classmethod
    def nodejs_files(cls):
        return [cls.TYPESCRIPT.value, cls.JAVASCRIPT.value]

    @classmethod
    def supported_files(cls):
        return [cls.TYPESCRIPT.value, cls.JAVASCRIPT.value, cls.PYTHON.value]