import openai
from openai import OpenAI

from BuckTheDuck.common.generative_ai.base_generative_ai import BaseGenerativeAI
from BuckTheDuck.common.generative_ai.config import Config
from BuckTheDuck.common.generative_ai.gen_ai_type import GenAiType


class OpenAiAccessor(BaseGenerativeAI):

    def __init__(self, context_message_prefix: str, context_message_suffix: str, open_chat_flag: bool):
        super().__init__(context_message_prefix, context_message_suffix, open_chat_flag)
        self.initial_conversation = True

    def _create_client(self):
        config = Config()
        client = OpenAI(
            # This is the default and can be omitted
            api_key=self._get_proper_token(GenAiType.OPENAI, config.generative_ais),
            base_url=None
        )
        return client

    def _send_message(self, message: str) -> str:
        if self.initial_conversation:
            message_input = [
                {
                    'role': 'system',
                    'content': self._context_message_prefix
                },
                {
                    'role': 'user',
                    'content': message
                },
                {
                    'role': 'system',
                    'content': self._context_message_prefix
                }
            ]
        else:
            message_input = [{
                    'role': 'user',
                    'content': message
                }]
        response = self._client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message_input
        )
        return response

    def __build_context_message(self, message: str):
        return message

    def _create_chat(self):
        pass
