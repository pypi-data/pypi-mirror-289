from BuckTheDuck import get_logger

from BuckTheDuck.generative_ai.generator_interface import GeneratorInterface
from BuckTheDuck.common.git.git_providers.parsers.git_log import GitLog

logger = get_logger()


class TicketProgressGenerator(GeneratorInterface):
    _LOG_PREFIX = 'TicketProgressGenerator'
    _COMMIT_ROLES = {
        'SINGLE_COMMENT': {
            'PREFIX': 'You are a skilled developer and you are about to merge your git branch back to source\n'
                      'Please summarize the your changes for the project manager',
            'SUFFIX': 'comment in a format of readable overall summary in few bullet points'
        },
        'SUMMARIZE': {
            'PREFIX': 'Please summarize the below text',
            'SUFFIX': 'comment in a format of readable overall summary in few bullet points'
        }
    }

    def generate_message(self, branch_commits: GitLog) -> str:
        diff_changes = ''
        work_summarized_comment = ''
        for commit in branch_commits.commits:
            if len(diff_changes) > 1000:
                progress_message_genai_response = self._do_request_with_strategy(self._generative_ai_strategy_for_commenting,
                                                                   'send_message', message=diff_changes)
                work_summarized_comment += progress_message_genai_response.text + '\n'
                diff_changes = ''
            else:
                diff_changes += commit

        if len(diff_changes) > 0:
            progress_message_genai_response = self._do_request_with_strategy(self._generative_ai_strategy_for_commenting,
                                                               'send_message', message=diff_changes)
            work_summarized_comment += progress_message_genai_response.text

        if len(work_summarized_comment.split('\n')) > self._MAX_NUMBER_OF_ROWS_FOR_COMMIT:
            finalized_commit_message = self._do_request_with_strategy(self._generative_ai_strategy_for_auditing,
                                                        'send_message', message=work_summarized_comment)
            work_summarized_comment = finalized_commit_message.text

        logger.info(f'{self._LOG_PREFIX}: Branch changes summary: {work_summarized_comment}')
        return work_summarized_comment
