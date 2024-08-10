from typing import List

from BuckTheDuck.common.generative_ai.base_generative_ai import BaseGenerativeAI
from BuckTheDuck.common.generative_ai.config import Config
from BuckTheDuck.common.generative_ai.gemini_accessor import GeminiAccessor
from BuckTheDuck.common.generative_ai.gen_ai_type import GenAiType
from BuckTheDuck.common.generative_ai.openai_accessor import OpenAiAccessor


class GenerativeAiStrategy:

    @classmethod
    def get_strategy(cls, context_message_prefix: str,
                     context_message_suffix: str, open_chat_flag: bool) -> List[BaseGenerativeAI]:
        config = Config()
        generative_ais = []
        for gen_ai_config in config.generative_ais:
            gen_ai_type = gen_ai_config.type
            if gen_ai_type == GenAiType.GEMINI:
                generative_ais.append(GeminiAccessor(context_message_prefix, context_message_suffix, open_chat_flag))
            elif gen_ai_type == GenAiType.OPENAI:
                generative_ais.append(OpenAiAccessor(context_message_prefix, context_message_suffix, open_chat_flag))
            else:
                raise NotImplemented(f'Gen AI - {gen_ai_type} not supported yet')

        return generative_ais
