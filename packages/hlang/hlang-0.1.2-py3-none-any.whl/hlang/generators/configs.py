import dataclasses

from typing import Optional, Iterable, Literal, Union, List
import httpx
from openai import NotGiven, NOT_GIVEN
from openai.types.chat import ChatCompletionStreamOptionsParam, completion_create_params


class BaseConfig:
    def __getattr__(self, name):
        return NOT_GIVEN


@dataclasses.dataclass
class OpenAIGenerationBaseConfig(BaseConfig):
    frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN
    function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN
    functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN
    logit_bias: Optional[dict[str, int]] | NotGiven = NOT_GIVEN
    logprobs: Optional[bool] | NotGiven = NOT_GIVEN
    max_tokens: Optional[int] | NotGiven = NOT_GIVEN
    n: Optional[int] | NotGiven = NOT_GIVEN
    presence_penalty: Optional[float] | NotGiven = NOT_GIVEN
    seed: Optional[int] | NotGiven = NOT_GIVEN
    service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN
    stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN
    temperature: Optional[float] | NotGiven = NOT_GIVEN
    top_logprobs: Optional[int] | NotGiven = NOT_GIVEN
    top_p: Optional[float] | NotGiven = NOT_GIVEN
    user: str | NotGiven = NOT_GIVEN
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN


@dataclasses.dataclass
class OpenAIGenerationStreamConfig(OpenAIGenerationBaseConfig):
    stream_options: ChatCompletionStreamOptionsParam = NotGiven
