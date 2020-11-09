from json import dump, loads
from codecs import open as opener

from CustomException import LoadNNException


class Saver:
    def __init__(self, file_path):
        self.__file_path = file_path

    def set_file_path(self, file_path):
        self.__file_path = file_path

    def get_file_path(self):
        return self.__file_path

    def save(self, data: dict):
        dump(
            data,
            opener(self.__file_path, 'w', encoding='utf-8'),
            separators=(',', ':'),
            sort_keys=True,
            indent=4
        )

    def load(self):
        try:
            obj = opener(self.__file_path, 'r', encoding='utf-8').read()
            return loads(obj)
        except FileNotFoundError as e:
            raise LoadNNException(e.filename)
