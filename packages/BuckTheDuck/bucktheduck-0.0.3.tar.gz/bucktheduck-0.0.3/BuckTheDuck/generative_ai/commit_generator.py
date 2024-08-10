from unidiff import PatchSet, PatchedFile

from BuckTheDuck import get_logger
from BuckTheDuck.common.file_path_utilities import FilePathUtilities
from BuckTheDuck.extractors.types.extracted_commit_changes import ExtractedCommitChanges
from BuckTheDuck.extractors.types.supported_languages import SupportedLanguages
from BuckTheDuck.generative_ai.generator_interface import GeneratorInterface

logger = get_logger()


class CommitGenerator(GeneratorInterface):
    _LOG_PREFIX = 'CommitGenerator'
    _COMMIT_ROLES = {
        'SINGLE_COMMENT': {
            'PREFIX': 'You are a skilled developer and you are about '
                      'to create a commit message for the following changes:',
            'SUFFIX': 'Please create meaningful commit message that summarize the changes and provide the overall effect of the changes'
        },
        'SUMMARIZE': {
            'PREFIX': 'You are a skilled developer and review your commit changes and want to make them shorter focus on the overall changes ',
            'SUFFIX': ''
        }
    }

    def generate_commit_message(self, summarized_changes: ExtractedCommitChanges) -> str:
        diff_changes = ''
        file: PatchedFile
        commit_message = ''
        for file_changes in summarized_changes.files_added:
            diff_changes += f'new class: {file_changes}\n'
        for file_changes in summarized_changes.files_changed:
            diff_changes += f'edited class: {file_changes}\n'
        for file_changes in summarized_changes.files_removed:
            diff_changes += f'removed class: {file_changes}\n'

        if len(diff_changes) > 0:
            commit_message_genai_response = self._do_request_with_strategy(self._generative_ai_strategy_for_commenting, 'send_message', message=diff_changes)
            commit_message += commit_message_genai_response.text

        logger.info(f'{self._LOG_PREFIX}: {commit_message=}')
        if len(commit_message.split('\n')) > self._MAX_NUMBER_OF_ROWS_FOR_COMMIT:
            finalized_commit_message = self._do_request_with_strategy(self._generative_ai_strategy_for_auditing,
                                                             'send_message', message=diff_changes)
            commit_message = finalized_commit_message.text

        commit_message = self._validate_with_user(commit_message)

        return commit_message

    def generate_commit_message_from_patchset(self, patchset: PatchSet) -> str:
        diff_changes = ''
        file: PatchedFile
        commit_message = ''
        for file in patchset:
            file_extension = FilePathUtilities.extract_file_extension(file.path)
            if not file_extension or file_extension in SupportedLanguages.supported_files():
                continue
            if len(diff_changes) > 1000:
                commit_message_genai_response = self._do_request_with_strategy(self._generative_ai_strategy_for_commenting, 'send_message', message=diff_changes)
                commit_message += commit_message_genai_response.text + '\n'
                diff_changes = ''
            else:
                if file.is_added_file:
                    diff_changes += (f'new file: {file.path}\n' + str(file))
                elif file.is_modified_file:
                    diff_changes += (f'modified file: {file.path}\n' + str(file))
                elif file.is_removed_file:
                    diff_changes += f'removed file: {file.path}'
                else:
                    continue
                diff_changes += '\n\n'

        if len(diff_changes) > 0:
            commit_message_genai_response = self._do_request_with_strategy(self._generative_ai_strategy_for_commenting, 'send_message', message=diff_changes)
            commit_message += commit_message_genai_response.text

        logger.info(f'{self._LOG_PREFIX}: {commit_message=}')
        if len(commit_message.split('\n')) > self._MAX_NUMBER_OF_ROWS_FOR_COMMIT:
            finalized_commit_message = self._do_request_with_strategy(self._generative_ai_strategy_for_auditing,
                                                        'send_message', message=diff_changes)
            commit_message = finalized_commit_message.text
        if commit_message:
            commit_message = self._validate_with_user(commit_message)

        return commit_message

    def _validate_with_user(self, commit_message):
        if self._open_chat_flag:
            print(f'Per your changes, this is the commit I suggest:\n{commit_message}')
            while True:
                user_feedback = input('Does that sounds good? Y/N')
                if not user_feedback or user_feedback.lower() == 'y':
                    break
                elif user_feedback.lower() not in ['y', 'n']:
                    print('Please choose Y/N')
                    continue
                else:
                    user_feedback = input('How can I describe the changes better?')
                    finalized_commit_message = self._do_request_with_strategy(self._generative_ai_strategy_for_auditing,
                                                                'send_message', message=user_feedback)
                    commit_message = finalized_commit_message.text
                    print(f'Per your feedback, this is the commit I suggest:\n{commit_message}')
        return commit_message
