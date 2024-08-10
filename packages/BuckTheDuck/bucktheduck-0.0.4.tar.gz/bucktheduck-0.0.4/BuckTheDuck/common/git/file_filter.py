from typing import List

from unidiff import PatchSet
from BuckTheDuck import get_logger

logger = get_logger()


class FileFilter:
    _LOG_PREFIX = 'FileFilter'

    def __init__(self, supported_file_types: List[str]):
        self._supported_file_types = supported_file_types

    def filter(self, git_difference: PatchSet):
        if not self._supported_file_types:
            return
        files_to_filter_index = []
        for index, git_change_file in enumerate(git_difference):
            filter_file = True
            for file_type in self._supported_file_types:
                if git_change_file.path.endswith(file_type):
                    filter_file = False
                    break
            if filter_file:
                files_to_filter_index.append(index)

        files_to_filter_index.reverse()
        for file_to_remove_index in files_to_filter_index:
            logger.info(f'{self._LOG_PREFIX}: filtering git_change_file {git_difference[file_to_remove_index].path}')
            git_difference.pop(file_to_remove_index)
