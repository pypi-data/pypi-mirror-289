import os

from openai import Client, AsyncClient

MOCK_KEY = 'sk-1234567890abcdef1234567890abcdef'


class LazyClientMixin:
    def __init__(self, **kwargs):
        api_key = kwargs.pop('api_key', None)
        super().__init__(
            api_key=MOCK_KEY,
            **kwargs
        )
        self._inited_real_key = False
        if api_key:
            self.api_key = api_key
            self._inited_real_key = True

    def set_key(self):
        if not self._inited:
            self.api_key = os.getenv('OPENAI_API_KEY')
            self._inited_real_key = True

    def __getattribute__(self, name):
        # Intercept attribute access
        if name != 'set_key' and callable(super().__getattribute__(name)):
            # Call set_key before any method other than set_key itself
            self.set_key()
        return super().__getattribute__(name)


class OpenAILazyClient(Client, LazyClientMixin):
    pass


class OpenAILazyAClient(AsyncClient, LazyClientMixin):
    pass
