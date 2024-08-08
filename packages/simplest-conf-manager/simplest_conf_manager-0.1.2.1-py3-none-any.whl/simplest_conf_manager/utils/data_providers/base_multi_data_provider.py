from abc import ABC
from typing import Type

from simplest_conf_manager.utils.data_providers.base_data_provider import BaseDataProvider


class BaseMultiDataProvider(BaseDataProvider, ABC):
    metalabel = '__multidata__'
    block_sep = '\t__block__\t'
    key_payload_sep = '\t__keypayload__\t'

    def __init__(self, _in_provider_cls: Type[BaseDataProvider]):
        self._in_provider_cls = _in_provider_cls
        BaseDataProvider.__init__(self)

    def get_providers(self, *args: list[dict]) -> list[BaseDataProvider]:
        return [self._in_provider_cls(**provider_data) for provider_data in args]


