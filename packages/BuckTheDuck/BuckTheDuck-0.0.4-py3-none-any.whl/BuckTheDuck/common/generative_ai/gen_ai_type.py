from enum import Enum
from typing import List


class GenAiType(Enum):
    GEMINI = 'gemini'
    OPENAI = 'openai'

    @classmethod
    def supported_gen_ai(cls) -> List[str]:
        return [GenAiType.GEMINI.value, GenAiType.OPENAI.value]