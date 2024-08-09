from BuckTheDuck.common.generative_ai.base_generative_ai import BaseGenerativeAI
from BuckTheDuck.common.generative_ai.gemini_accessor import GeminiAccessor
from BuckTheDuck.common.generative_ai.config import Config
from BuckTheDuck.common.generative_ai.gen_ai_type import GenAiType
from BuckTheDuck.common.generative_ai.openai_accessor import OpenAiAccessor


class GenerativeAiFactory:

    @classmethod
    def get_accessor(cls, context_message_prefix: str,
                     context_message_suffix: str, open_chat_flag: bool) -> BaseGenerativeAI:
        config = Config()
        gen_ai_type = config.generative_ais[0].type
        if gen_ai_type == GenAiType.GEMINI:
            return GeminiAccessor(context_message_prefix, context_message_suffix, open_chat_flag)
        elif gen_ai_type == GenAiType.OPENAI:
            return OpenAiAccessor(context_message_prefix, context_message_suffix, open_chat_flag)
        else:
            raise NotImplemented(f'Gen AI - {gen_ai_type} not supported yet')