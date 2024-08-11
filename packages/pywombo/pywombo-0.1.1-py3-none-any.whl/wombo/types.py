from proxystr.adapter import _ExtraTypeConstructor
from pydantic.networks import HttpUrl as BaseHttpUrl


class HttpUrl(str, metaclass=_ExtraTypeConstructor):
    @classmethod
    def validate(cls, v):
        return BaseHttpUrl(v).__str__()
