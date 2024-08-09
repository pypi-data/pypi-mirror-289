import os
import google.generativeai as genai

from BuckTheDuck.common.generative_ai.base_generative_ai import BaseGenerativeAI
from BuckTheDuck.common.generative_ai.config import Config
from BuckTheDuck.common.generative_ai.gen_ai_type import GenAiType


class GeminiAccessor(BaseGenerativeAI):

    def _create_client(self):
        config = Config()
        GOOGLE_API_KEY = self._get_proper_token(GenAiType.GEMINI, config.generative_ais)
        genai.configure(api_key=GOOGLE_API_KEY)
        return genai.GenerativeModel('gemini-pro')

    def _send_message(self, message: str) -> str:
        self._create_chat()
        response = self._chat.send_message(message, stream=self._open_chat_flag)
        response.resolve()
        return response

    def _create_chat(self):
        if self._chat is None:
            self._chat = self._client.start_chat(history=[])
