from unidiff import PatchSet, PatchedFile

from BuckTheDuck import get_logger

from BuckTheDuck.generative_ai.generator_interface import GeneratorInterface

logger = get_logger()


class CodeReviewerGenerator(GeneratorInterface):
    _LOG_PREFIX = 'CodeReviewerGenerator'
    _COMMIT_ROLES = {
        'SINGLE_COMMENT': {
            'PREFIX': 'You are an experience Software Developer. Your input is git diff. '
                      'Please provide code review on the following changes. '
                      'The priority is naming conventions, keep it short',
            'SUFFIX': 'Again keep it short and summarize the changes you wish to have in a single paragraph'
        },
        'SUMMARIZE': {
            'PREFIX': '',
            'SUFFIX': ''
        }
    }

    def generate_message(self, git_difference: PatchSet):
        file: PatchedFile
        code_review_message = ''
        for file in git_difference:
            diff_changes = ''
            if file.is_rename:
                continue
            elif file.is_added_file:
                diff_changes += (f'new file: {file.path}\n' + str(file))
            elif file.is_modified_file:
                diff_changes += (f'modified file: {file.path}\n' + str(file))
            elif file.is_removed_file:
                diff_changes += f'removed file: {file.path}'
            commit_message_genai_response = self._do_request_with_strategy(self._generative_ai_strategy_for_commenting, 'send_message', message=diff_changes)
            code_review_message += f'{file.path}:\n{commit_message_genai_response}\n\n'
            logger.info(f'{self._LOG_PREFIX}: Code review for {file.path}: {code_review_message}')
            print(f'{self._LOG_PREFIX}: Code review for {file.path}: {code_review_message}')

        return code_review_message
