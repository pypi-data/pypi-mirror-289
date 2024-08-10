import textwrap

from abc import ABC, abstractmethod
from typing import List

import throttle
from IPython.display import Markdown

from BuckTheDuck.common.generative_ai.config import GenAiConfig
from BuckTheDuck.common.generative_ai.gen_ai_type import GenAiType


class BaseGenerativeAI(ABC):
    __MINUTE_IN_SECONDS = 60
    __NUMBER_OF_QUESTION_IN_TIME_FRAME = 10

    def __init__(self, context_message_prefix: str, context_message_suffix: str, open_chat_flag: bool):
        self._open_chat_flag = open_chat_flag
        self._context_message_suffix = context_message_suffix
        self._context_message_prefix = context_message_prefix
        self.__client = None
        self._chat = None

    @property
    def _client(self):
        if self.__client is None:
            self.__client = self._create_client()
        return self.__client

    @throttle.wrap(__MINUTE_IN_SECONDS, __NUMBER_OF_QUESTION_IN_TIME_FRAME)
    def send_message(self, message: str):
        message = self.__build_context_message(message)
        return self._send_message(message)

    def __build_context_message(self, message: str):
        return self._context_message_prefix + '\n' + message + '\n' + self._context_message_suffix

    @abstractmethod
    def _send_message(self, message: str):
        pass

    @abstractmethod
    def _create_client(self):
        pass

    @abstractmethod
    def _create_chat(self):
        pass

    def to_markdown(self, text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    def _get_proper_token(self, gen_ai_type: GenAiType, gen_ai_configs: List[GenAiConfig]):
        for genai_config in gen_ai_configs:
            if genai_config.type == gen_ai_type:
                return genai_config.token