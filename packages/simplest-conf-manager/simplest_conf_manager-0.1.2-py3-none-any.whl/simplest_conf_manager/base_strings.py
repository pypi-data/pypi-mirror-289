from abc import ABC

from simplest_conf_manager import BaseConfig


class BaseStrings(BaseConfig, ABC):
    langs: dict

    def __getattr__(self, item):
        if item in self.langs:
            return self.langs[item]
        raise AttributeError(f"'Strings' object has no attribute '{item}'")

    def __setattr__(self, key, value):
        if key == "langs":
            super().__setattr__(key, value)
        else:
            self.langs[key] = value
