from dataclasses import dataclass
from typing import List

from BuckTheDuck.common.singleton import Singleton
from BuckTheDuck.common.generative_ai.gen_ai_type import GenAiType


@dataclass
class GenAiConfig:
    type: GenAiType
    token: str


class Config(Singleton):
    _supported_file_types = []
    _generative_ais: List[GenAiConfig] = []

    @property
    def generative_ais(self):
        return self._generative_ais

    def add_gen_ai(self, gen_ai_type_str: str, token: str):
        gen_ai_type = GenAiType[gen_ai_type_str.upper()]
        self._generative_ais.append(GenAiConfig(gen_ai_type, token))

    @property
    def supported_file_types(self):
        return self._supported_file_types

    @supported_file_types.setter
    def supported_file_types(self, supported_file_types: List[str]):
        self._supported_file_types = supported_file_types
