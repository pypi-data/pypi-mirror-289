import os
from openai import Client, AsyncClient

MOCK_KEY = 'sk-1234567890abcdef1234567890abcdef'


class LazyClientMixin:
    def __init__(self, api_key=None):
        self._inited_real_key = False
        self.api_key = api_key or MOCK_KEY
        if api_key:
            self._inited_real_key = True

    def set_key(self):
        if not self._inited_real_key:
            real_key = os.getenv('OPENAI_API_KEY')
            if real_key:
                self.api_key = real_key
                self._inited_real_key = True

    def __getattribute__(self, name):
        if name not in ['set_key', '_inited_real_key', 'api_key'] and callable(super().__getattribute__(name)):
            self.set_key()
        return super().__getattribute__(name)


class OpenAILazyClient(LazyClientMixin, Client):
    def __init__(self, **kwargs):
        api_key = kwargs.pop('api_key', None)
        LazyClientMixin.__init__(self, api_key)
        Client.__init__(self, api_key=self.api_key, **kwargs)


class OpenAILazyAClient(LazyClientMixin, AsyncClient):
    def __init__(self, **kwargs):
        api_key = kwargs.pop('api_key', None)
        LazyClientMixin.__init__(self, api_key)
        AsyncClient.__init__(self, api_key=self.api_key, **kwargs)
