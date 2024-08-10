from BuckTheDuck import get_logger
from BuckTheDuck.documentor.file_mapping import FileMapping
from BuckTheDuck.generative_ai.generator_interface import GeneratorInterface

logger = get_logger()


class SummarizeFileGenerator(GeneratorInterface):
    _LOG_PREFIX = 'CommitGenerator'
    _COMMIT_ROLES = {
        'SINGLE_COMMENT': {
            'PREFIX': 'You are a software developer and you are about '
                      'to document your code, your input is the class name and some methods',
            'SUFFIX': 'Please create meaningful markdown message that summarize the above text'
        },
        'SUMMARIZE': {
            'PREFIX': 'You are a skilled developer and review your markdown changes and want to make them shorter',
            'SUFFIX': ''
        }
    }

    def __init__(self):
        super().__init__(open_chat_flag=True)

    def generate_markdown(self, file_mapping: FileMapping):
        message = f'Class name {file_mapping.class_name}\n'
        markdown = ''
        for public_method in file_mapping.public_methods:
            message += public_method.method_content + '\n'
            if len(message) > 1000:
                markdown += self._do_request_with_strategy(self._generative_ai_strategy_for_commenting, 'send_message',
                                                           message=message).text
                markdown += '\n'
            message = ''
        if message:
            markdown += self._do_request_with_strategy(self._generative_ai_strategy_for_commenting, 'send_message',
                                                       message=message).text
            markdown += '\n'
        return markdown
