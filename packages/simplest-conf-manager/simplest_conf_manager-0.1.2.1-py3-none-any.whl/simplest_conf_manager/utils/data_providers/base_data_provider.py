from abc import ABC, abstractmethod


class BaseDataProvider(ABC):
    def __init__(self, **kwargs):
        ...

    @abstractmethod
    def get_data(self) -> str:
        ...
