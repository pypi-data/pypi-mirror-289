import os

from simplest_conf_manager.utils.data_providers.base_multi_data_provider import BaseMultiDataProvider
from simplest_conf_manager.utils.data_providers.file_data_provider import FileDataProvider


class FolderDataProvider(BaseMultiDataProvider, FileDataProvider):
    def __init__(self, path: str, modifier: str = 'r', encoding: str = 'utf-8'):
        FileDataProvider.__init__(self, path, modifier, encoding)
        BaseMultiDataProvider.__init__(self, FileDataProvider)

    def _get_file_paths(self) -> dict[str, str]:
        files = os.listdir(self.path)
        paths = {file_name: path
                    for file_name, path in
                        zip(files,
                            filter(lambda s: os.path.isfile(s),
                                   map(lambda s: os.path.join(self.path, s),
                                       files)))}
        return paths

    def get_data(self) -> str:
        file_paths = self._get_file_paths()
        providers = self.get_providers(*({'path': path,
                                         'modifier': self.modifier,
                                         'encoding': self.encoding} for path in file_paths.values()))
        return self.metalabel +\
            self.block_sep.join(block for block in [self.key_payload_sep.join((file_name.rsplit('.', maxsplit=1)[0], provider.get_data()))
                                                    for file_name, provider in zip(file_paths.keys(), providers)])
