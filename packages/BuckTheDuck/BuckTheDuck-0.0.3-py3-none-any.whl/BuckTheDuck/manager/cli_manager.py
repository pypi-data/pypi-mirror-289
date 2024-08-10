import logging
import os
from enum import Enum
from pathlib import Path
from typing import List

from BuckTheDuck import set_logger_level
from BuckTheDuck.common.git.git_providers.git_accessor import GitAccessor
from BuckTheDuck.documentor.documentation_manager import DocumentationManager
from BuckTheDuck.extractors.extractor_factory import ExtractorFactory
from BuckTheDuck.extractors.types.extracted_commit_changes import ExtractedCommitChanges
from BuckTheDuck.extractors.types.supported_languages import SupportedLanguages
from BuckTheDuck.generative_ai.commit_generator import CommitGenerator
from BuckTheDuck.manager.config_manager import ConfigManager
from BuckTheDuck.common.exceptions import UnsupportedOperation
from BuckTheDuck.generative_ai.code_reviewer_generator import CodeReviewerGenerator
from BuckTheDuck.generative_ai.ticket_progress_generator import TicketProgressGenerator


class CliManager:
    HOME = '~'
    _SUPPORTED_FLAGS = {
        'commit': ['-c', '--chat'],
        'verbose': ['-v', '--verbose']
    }

    def __init__(self):
        self._config_manager = ConfigManager()

    def run(self, command: str, argv: List[str]):
        self._toggle_verbose(argv)
        if command not in AvailableCommands.to_list():
            command = AvailableCommands.HELP.value
        if command == AvailableCommands.INIT.value:
            self._init_env()
        if command == AvailableCommands.FILE_CONTROL.value:
            self._manage_file_control()
        if command == AvailableCommands.HELP.value:
            self._print_help_menu()
        self._config_manager.load_config()
        if command == AvailableCommands.COMMIT.value:
            self._commit_changes(argv)
        if command == AvailableCommands.COMMIT_AND_PUSH.value:
            self._commit_and_push(argv)
        if command == AvailableCommands.BRANCH_SUMMARIZE.value:
            self._summarize_branch_changes(argv)
        if command == AvailableCommands.CODE_REVIEW.value:
            self._run_code_review()
        if command == AvailableCommands.SUMMARIZE_REPO.value:
            self._run_summarize()

    def _print_help_menu(self):
        print('Available Commands: ')
        print('1. init - Initiate Buck to work with your favorite GenAI provider  ')
        print('2. commit - Generate commit message per your changes and commit it  ')
        print('3. cop - Generate commit message per your changes and commit & push it  ')
        print('4. branch_summarize - Generate message for your changes in a '
              'branch before merging back to source branch  ')
        print('5. code review - Generate a code review feedback ')
        print('6. help - List available commands')

    def _normalize_path(self, path):
        if '~' in path:
            path = path.replace(self.HOME, str(Path.home()))
        return path

    def _commit_changes(self, argv: List[str]):
        open_chat_flag = False
        if len(argv) > 1:
            raise UnsupportedOperation('Too many flags for commit command')
        if argv and argv[0] in self._SUPPORTED_FLAGS['commit']:
            open_chat_flag = True
        elif argv[0] and argv[0] not in self._SUPPORTED_FLAGS['commit']:
            raise UnsupportedOperation(f'{argv[0]} flag not supported please use {self._SUPPORTED_FLAGS["commit"]}')

        current_working_directory = os.getcwd()
        git_accessor = GitAccessor(current_working_directory, current_working_directory)
        patch_set = git_accessor.get_last_commit_differences()
        branch_name = git_accessor.get_branch_name()
        python_code_extractor = ExtractorFactory().create(SupportedLanguages.PYTHON)
        nodejs_code_extractor = ExtractorFactory().create(SupportedLanguages.TYPESCRIPT)
        extracted_commit_changes = ExtractedCommitChanges([], [], [])
        python_code_extractor.extract_from_commits(patch_set, extracted_commit_changes)
        nodejs_code_extractor.extract_from_commits(patch_set, extracted_commit_changes)
        commit_generator = CommitGenerator(open_chat_flag)
        commit_message = commit_generator.generate_commit_message(extracted_commit_changes)
        commit_message += commit_generator.generate_commit_message_from_patchset(patch_set)
        commit_message = f'branch name: {branch_name}\n' + commit_message
        git_accessor.commit(commit_message)

    def _commit_and_push(self, argv):
        self._commit_changes(argv)
        current_working_directory = os.getcwd()
        git_accessor = GitAccessor(current_working_directory, current_working_directory)
        git_accessor.push()

    def _init_env(self):
        config_manager = ConfigManager()
        config_manager.init()

    def _summarize_branch_changes(self, argv):
        try:
            branch_name = argv[0]
            source_branch_name = argv[1]
        except:
            raise UnsupportedOperation('This command require argument for branch name')
        current_working_directory = os.getcwd()
        git_accessor = GitAccessor(current_working_directory, current_working_directory)
        gitlog = git_accessor.get_branch_changes(branch_name, source_branch_name)
        ticket_progress_generator = TicketProgressGenerator()
        message = ticket_progress_generator.generate_message(gitlog)
        # TODO: need to add connector to project management (JIRA and friends)

    def _run_code_review(self):
        current_working_directory = os.getcwd()
        git_accessor = GitAccessor(current_working_directory, current_working_directory)
        patch_set = git_accessor.get_last_commit_differences()
        code_review_generator = CodeReviewerGenerator()
        code_review_generator.generate_message(patch_set)

    def _manage_file_control(self):
        config_manager = ConfigManager()
        config_manager.file_manager()

    def _run_summarize(self):
        current_working_directory = os.getcwd()
        document_manager = DocumentationManager()
        document_manager.document_project(current_working_directory)

    def _toggle_verbose(self, argv):
        index_to_pop = -1
        log_level = logging.WARNING
        for index, argument in enumerate(argv):
            if argument in self._SUPPORTED_FLAGS['verbose']:
                index_to_pop = index
                log_level = logging.INFO

        set_logger_level(log_level=log_level)
        argv.pop(index_to_pop)


class AvailableCommands(Enum):
    HELP = 'help'
    INIT = 'init'
    FILE_CONTROL = 'file_control'
    COMMIT = 'commit'
    PUSH = 'push'
    COMMIT_AND_PUSH = 'cop'
    BRANCH_SUMMARIZE = 'branch_summarize'
    CODE_REVIEW = 'cr'
    SUMMARIZE_REPO = 'summarize_repo'

    @classmethod
    def to_list(cls):
        return [cls.HELP.value,
                cls.COMMIT.value,
                cls.COMMIT_AND_PUSH.value,
                cls.INIT.value,
                cls.FILE_CONTROL.value,
                cls.BRANCH_SUMMARIZE.value,
                cls.CODE_REVIEW.value,
                cls.SUMMARIZE_REPO.value]