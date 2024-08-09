import json
import os
from enum import Enum
from getpass import getpass
from pathlib import Path

from BuckTheDuck.common.exceptions import UnsupportedOperation
from BuckTheDuck.common.generative_ai.config import Config
from BuckTheDuck.common.generative_ai.gen_ai_type import GenAiType


class ConfigKeys(Enum):
    GENAI_ARRAY = 'genais'
    GENAI_TYPE = 'genai_type'
    GENAI_TOKEN = 'genai_token'
    SUPPORTED_FILES = 'SUPPORTED_FILES'


class ConfigManager:
    _CONFIG_DIR = f'{Path.home()}/.BuckTheDuck'

    def init(self):
        if not os.path.exists(self._CONFIG_DIR):
            self._init_config_file()

        self._add_project()
        self._add_supported_files()

    def load_config(self):
        config = self._load_config_file()
        config_instance = Config()
        if ConfigKeys.GENAI_ARRAY.value in config and ConfigKeys.SUPPORTED_FILES.value in config:
            for gen_ai_config in config[ConfigKeys.GENAI_ARRAY.value]:
                config_instance.add_gen_ai(gen_ai_config[ConfigKeys.GENAI_TYPE.value], gen_ai_config[ConfigKeys.GENAI_TOKEN.value])
            config_instance.supported_file_types = config.get(ConfigKeys.SUPPORTED_FILES.value, [])
        else:
            print(f'We are missing an parameter to start working, please run again the \'init\' command')
            raise UnsupportedOperation()

    def _load_config_file(self):
        try:
            with open(f'{self._CONFIG_DIR}/config', 'r') as config_file:
                config = json.load(config_file)
        except FileNotFoundError:
            config = {
                ConfigKeys.GENAI_ARRAY.value: [],
                ConfigKeys.SUPPORTED_FILES.value: []
            }
        return config

    def _init_config_file(self):
        os.mkdir(self._CONFIG_DIR)
        config = {
            ConfigKeys.GENAI_ARRAY.value: [],
            ConfigKeys.SUPPORTED_FILES.value: []
        }
        self._write_content_to_config_file(config)

    def _add_project(self):
        config = self._load_config_file()

        genai_type_input = input(f'Enter Gen AI type: {GenAiType.supported_gen_ai()} ')
        if genai_type_input not in GenAiType.supported_gen_ai():
            print(f'{genai_type_input} is not a supported Gen AI type, but soon it will!')
            raise UnsupportedOperation()
        genai_token = getpass('Enter Gen AI Token: ')
        existing_gen_ais = [gen_ai_config[ConfigKeys.GENAI_TYPE.value] for gen_ai_config in config[ConfigKeys.GENAI_ARRAY.value]]
        is_new_config = genai_type_input not in existing_gen_ais
        if is_new_config:
            config[ConfigKeys.GENAI_ARRAY.value].append({
                ConfigKeys.GENAI_TYPE.value: genai_type_input,
                ConfigKeys.GENAI_TOKEN.value: genai_token
            })
        else:
            override_config = self._do_we_need_to_override_config(existing_gen_ais, genai_type_input)
            if override_config:
                config[ConfigKeys.GENAI_ARRAY.value][existing_gen_ais.index(genai_type_input)] = {
                    ConfigKeys.GENAI_TYPE.value:  genai_type_input,
                    ConfigKeys.GENAI_TOKEN.value: genai_token
                }

        self._write_content_to_config_file(config)

    def _do_we_need_to_override_config(self, existing_gen_ais, genai_type_input):
        write_config = True
        if genai_type_input in existing_gen_ais:
            while True:
                user_input_for_override_config = input(f'I see you have a config for {genai_type_input}, do you wish to override it? (Y/N)')
                if user_input_for_override_config.upper() not in ['Y', 'N']:
                    print('Please choose Y/N as your option')
                    continue
                write_config = user_input_for_override_config == 'Y'
                break
        return write_config

    def _write_content_to_config_file(self, config):
        with open(f'{self._CONFIG_DIR}/config', 'w') as config_file:
            config_file.write(json.dumps(config))

    def _add_supported_files(self):
        config = self._load_config_file()
        while True:
            file_types_input = input(f'What kind of file type you wish me to read? you can '
                                     f'use comma separation between inputs')
            file_types = file_types_input.split(',')
            user_response = input(f'I will be scanning only files from type {file_types}, is that correct? Y/N')
            if not user_response or user_response.lower() == 'y':
                break

        config[ConfigKeys.SUPPORTED_FILES.value] = file_types
        self._write_content_to_config_file(config)

    def file_manager(self):
        self._add_supported_files()
