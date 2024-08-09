from abc import ABC, abstractmethod
from typing import List, Tuple

from BuckTheDuck.documentor.file_mapping import FileMapping


class BaseLanguageParser(ABC):
    LOG_PREFIX = 'BaseLanguageParser'

    @abstractmethod
    def parse_file(self, file) -> FileMapping:
        raise NotImplemented

    @abstractmethod
    def _get_class_name(self, line) -> str:
        raise NotImplemented

    @abstractmethod
    def _get_method_name(self, line) -> str:
        raise NotImplemented

    @abstractmethod
    def _is_public_method(self, method_name) -> bool:
        raise NotImplemented

    @abstractmethod
    def _get_method_arguments(self, line) -> List[str]:
        raise NotImplemented

    @abstractmethod
    def _get_method_boundaries(self, code_file) -> Tuple[int, int]:
        pass