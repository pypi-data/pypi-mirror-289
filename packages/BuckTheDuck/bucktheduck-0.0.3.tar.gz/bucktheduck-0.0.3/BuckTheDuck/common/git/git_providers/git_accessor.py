import subprocess
from typing import List

from pygit2 import Repository, GIT_SORT_TIME, Commit
from unidiff import PatchSet
from BuckTheDuck import get_logger
from BuckTheDuck.common.exceptions import FailedToCommit, FailedToPush
from BuckTheDuck.common.generative_ai.config import Config
from BuckTheDuck.common.git.file_filter import FileFilter
from BuckTheDuck.common.git.git_providers.parsers.git_log import GitLog

logger = get_logger()


class GitAccessor:
    _LOG_PREFIX = 'GitAccessor'

    def __init__(self, project_root_path: str, source_branch: str):
        self.source_branch = source_branch
        self.project_root_path = project_root_path
        self._repo = Repository(project_root_path)
        self._current_branch_name = None
        config = Config()
        self._file_filter = FileFilter(config.supported_file_types)

    @property
    def current_branch_name(self):
        if self._current_branch_name:
            return self._current_branch_name
        self._current_branch_name = self._repo.head.name
        return self._current_branch_name

    def get_commits(self) -> List[Commit]:
        commits = []
        commits_itr = self._repo.walk(self._repo.head.target, GIT_SORT_TIME)
        for commit in commits_itr:
            commits.append(commit)
            break
        return commits

    def get_last_commit_differences(self) -> PatchSet:
        cmd = 'git diff HEAD'
        result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
        raw_patch = result.stdout.decode('utf-8')
        patch_set = PatchSet.from_string(raw_patch)
        self._file_filter.filter(patch_set)
        return patch_set

    def commit(self, commit_message: str):
        logger.info(f'{self._LOG_PREFIX}: announcing commit with message: {commit_message}')
        cmd = f'git commit -am '
        result = subprocess.run(cmd.split() + [f'"{commit_message}"'], stdout=subprocess.PIPE)
        if result.returncode == 0:
            logger.info(f'{self._LOG_PREFIX}: Successful commit')
        else:
            error_message = f'Failed ot commit {result.returncode=}'
            logger.error(f'{self._LOG_PREFIX}: {error_message}')
            raise FailedToCommit(error_message)

    def push(self):
        branch_name = self.get_branch_name()
        cmd = 'git push'
        if branch_name:
            cmd += f' --set-upstream origin {branch_name}'
        result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
        if result.returncode == 0:
            logger.info(f'{self._LOG_PREFIX}: Successful commit')
        else:
            error_message = f'Failed ot commit {result.returncode=}'
            logger.error(f'{self._LOG_PREFIX}: {error_message}')
            raise FailedToPush(error_message)

    def get_branch_name(self):
        cmd = 'git branch --show-current'
        result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
        return result.stdout.decode().replace('\n', '')

    def get_branch_changes(self, branch_name, source_branch_name) -> GitLog:
        cmd = f'git log {source_branch_name}..{branch_name}'
        result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
        raw_patch = result.stdout.decode('utf-8')
        git_log = GitLog(raw_patch)
        return git_log
