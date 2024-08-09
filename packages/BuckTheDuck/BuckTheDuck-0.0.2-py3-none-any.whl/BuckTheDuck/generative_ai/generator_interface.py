from abc import ABC

from openai import RateLimitError

from BuckTheDuck import get_logger
from BuckTheDuck.common.generative_ai.generative_ai_strategy import GenerativeAiStrategy

logger = get_logger()


class GeneratorInterface(ABC):
    _LOG_PREFIX = 'GeneratorInterface'
    _MAX_NUMBER_OF_ROWS_FOR_COMMIT = 10
    _COMMIT_ROLES = {
        'SINGLE_COMMENT': {
            'PREFIX': '',
            'SUFFIX': ''
        },
        'SUMMARIZE': {
            'PREFIX': '',
            'SUFFIX': ''
        }
    }

    def __init__(self, open_chat_flag: bool = False):
        self._open_chat_flag = open_chat_flag
        self._generative_ai_strategy_for_commenting = (
            GenerativeAiStrategy.get_strategy(self._COMMIT_ROLES['SINGLE_COMMENT']['PREFIX'],
                                              self._COMMIT_ROLES['SINGLE_COMMENT']['SUFFIX'], open_chat_flag))
        self._generative_ai_strategy_for_auditing = (
            GenerativeAiStrategy.get_strategy(self._COMMIT_ROLES['SUMMARIZE']['PREFIX'],
                                              self._COMMIT_ROLES['SUMMARIZE']['SUFFIX'], open_chat_flag))

    def _do_request_with_strategy(self, strategy, method: str, gen_ai_index: int = 0, **kwargs):
        has_error_occurred = False
        try:
            accessor = strategy[gen_ai_index]
            return accessor.__getattribute__(method)(**kwargs)
        except RateLimitError:
            has_error_occurred = True
            logger.warning(f'{self._LOG_PREFIX}: OpenAI rate limit reached')
        except Exception as e:
            has_error_occurred = True
            logger.warning(f'{self._LOG_PREFIX}: Accessor got exception {e}, activating strategy')
        finally:
            if gen_ai_index >= len(strategy):
                logger.exception(f'{self._LOG_PREFIX}: Strategy depleted, raising')
                raise
            if has_error_occurred:
                return self._do_request_with_strategy(strategy, method, gen_ai_index + 1, **kwargs)
