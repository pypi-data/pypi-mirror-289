from pydantic import BaseModel

from simplest_conf_manager import BaseStrings


class Translator(BaseModel):
    strings: BaseStrings
    lang: str

    def __getattr__(self, key):
        if key in ('strings', 'lang'):
            return getattr(self.strings, key)
        try:
            return getattr(self.strings.langs[self.lang], key)
        except KeyError:
            if self.lang in self.strings.langs:
                raise AttributeError(f"No such attribute '{key}' in the '{self.lang}' language")
            else:
                raise AttributeError(f"Language '{self.lang}' is not supported")

    def __setattr__(self, key, value):
        if key in ('strings', 'lang'):
            setattr(self.strings, key, value)
        else:
            setattr(self.strings.langs[self.lang], key, value)
