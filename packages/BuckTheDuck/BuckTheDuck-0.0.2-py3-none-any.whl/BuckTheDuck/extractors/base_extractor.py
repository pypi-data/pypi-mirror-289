from abc import ABC, abstractmethod
from typing import List

from unidiff import PatchSet, PatchedFile

from BuckTheDuck.extractors.types.extracted_commit_changes import ExtractedCommitChanges, ChangeMapping


class BaseExtractor(ABC):

    _LOG_PREFIX = 'BaseExtractor'

    @abstractmethod
    def extract_from_commits(self, patch_set: PatchSet, extracted_commit_changes: ExtractedCommitChanges):
        pass

    @abstractmethod
    def _extract_changes(self, file: PatchedFile) -> List[ChangeMapping]:
        pass

    @abstractmethod
    def _extract_class_name_from_deleted_file(self, file: PatchedFile) -> str:
        pass