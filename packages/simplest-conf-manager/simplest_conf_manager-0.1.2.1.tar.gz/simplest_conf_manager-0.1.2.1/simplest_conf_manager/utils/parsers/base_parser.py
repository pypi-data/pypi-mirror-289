from abc import ABC, abstractmethod
from typing import Type, Optional

from simplest_conf_manager.utils.data_providers.base_data_provider import BaseDataProvider
from simplest_conf_manager.utils.data_providers.base_multi_data_provider import BaseMultiDataProvider


class BaseParser(ABC):  # type: ignore
    def __init__(self,
                 payload: Optional[str | BaseDataProvider] = None):
        self.payload = payload

    def parse(self,
              payload: Optional[str | BaseDataProvider] = None) -> dict:
        if payload is None:
            payload = self.payload

        if isinstance(payload, BaseDataProvider):
            payload: str = payload.get_data()

        if payload.startswith(BaseMultiDataProvider.metalabel):
            payload = payload.split(BaseMultiDataProvider.metalabel, maxsplit=1)[1]
            return self._parse_multi_data(payload)

        return self._parse(payload)

    def _parse_multi_data(self,
                          payload: str) -> dict:
        data = dict([keyvalue.split(BaseMultiDataProvider.key_payload_sep)
                     for keyvalue in payload.split(BaseMultiDataProvider.block_sep)])
        return {key: self._parse(value) for key, value in data.items()}

    @abstractmethod
    def _parse(self, payload: str) -> dict:
        ...
