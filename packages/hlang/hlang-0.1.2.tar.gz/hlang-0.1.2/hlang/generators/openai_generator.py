from typing import Iterable


from hlang.dataclasses.message import ChatMessage
from hlang.generators.configs import OpenAIGenerationBaseConfig, OpenAIGenerationStreamConfig
from hlang.generators.generator import ABCChatGenerator
from hlang.openai_lazy_client import OpenAILazyClient


class OpenAIChatGenerator(ABCChatGenerator):
    def __init__(self, model_name: str, base_url: str):
        self.client = OpenAILazyClient(base_url=base_url)
        self.model_name = model_name

    def generate(self,
                 messages: [ChatMessage],
                 config: OpenAIGenerationBaseConfig = OpenAIGenerationBaseConfig()
                 ) -> ChatMessage | Iterable[ChatMessage]:
        self._prompt_sanity_check(messages)
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[m.to_dict() for m in messages],
            frequency_penalty=config.frequency_penalty,
            function_call=config.function_call,
            functions=config.functions,
            logit_bias=config.logit_bias,
            logprobs=config.logprobs,
            max_tokens=config.max_tokens,
            n=config.n,
            presence_penalty=config.presence_penalty,
            seed=config.seed,
            service_tier=config.service_tier,
            stop=config.stop,
            stream=False,
            temperature=config.temperature,
            top_logprobs=config.top_logprobs,
            top_p=config.top_p,
            user=config.user,
            timeout=config.timeout
        )
        contents = [choice.message.content for choice in response.choices]
        if not config.n or config.n == 1:
            return ChatMessage.from_assistant(contents[0])
        return [ChatMessage.from_assistant(content) for content in contents]

    def stream(self,
               messages: [ChatMessage],
               config: OpenAIGenerationStreamConfig = OpenAIGenerationStreamConfig(),
               ) -> Iterable[str]:
        iterator = self.client.chat.completions.create(
            messages=[m.to_dict() for m in messages],
            model=self.model_name,
            frequency_penalty=config.frequency_penalty,
            function_call=config.function_call,
            functions=config.functions,
            logit_bias=config.logit_bias,
            logprobs=config.logprobs,
            max_tokens=config.max_tokens,
            presence_penalty=config.presence_penalty,
            seed=config.seed,
            service_tier=config.service_tier,
            stop=config.stop,
            stream=True,
            stream_options=config.stream_options,
            temperature=config.temperature,
            top_logprobs=config.top_logprobs,
            top_p=config.top_p,
            user=config.user,
            timeout=config.timeout
        )
        for chunk in iterator:
            yield chunk.choices[0].delta.content
