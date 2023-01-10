from DAO import FileDao
import re
from typing import Optional, Any, Iterable, TextIO

class FileService:
    def __init__(self, dao: FileDao) -> None:
        self._dao = dao
        self._result: Optional[Iterable | Any] = None

    def add_new_file(self, filename: str) -> None:
        self._dao.add_filename(filename)

    def filter(self, value: str) -> None:
        data = self._get_source()

        self._result = filter(lambda x: value in x, data)

    def filter_by_regex(self, regex: str) -> None:

        data = self._get_source()
        re_validator = re.compile(regex)

        self._result = filter(lambda x: bool(re_validator.search(x)), data)

    def map(self, value: str) -> None:
        data = self._get_source()

        try:
            column = int(value)
        except ValueError:
            column = 0

        self._result = map(lambda x: x.split(' ')[column] + '\n', data)

    def unique(self, value: Optional[Any] = None) -> None:

        data = self._get_source()

        self._result = iter(set(data))

    def sort(self, order: str = 'asc') -> None:
        if order not in ('asc', 'desc'):
            order = 'asc'

        data = self._get_source()

        self._result = sorted(data, reverse=False if order == 'asc' else True)

    def limit(self, value: str) -> None:
        data = self._get_source()

        try:
            amount = int(value)

        except ValueError:
            amount = 1

        limited = list(data)[:amount]
        self._result = iter(limited)

    def get_result(self) -> str:

        if self._result:
            result = ''.join(self._result)
            self._result = None
            return result

        return ''

    def _get_source(self) -> Iterable | TextIO:
        if self._result is None:
            data: Iterable | TextIO = self._dao.open()

        else:
            data = self._result

        return data
