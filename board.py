import gettext
from enum import Enum, auto, unique
from itertools import repeat
from typing import Any, List

_ = gettext.gettext

NUMBER_FIELDS = 9


@unique
class Field(Enum):
    EMPTY = auto()
    CIRCLE = auto()
    CROSS = auto()


class NumFieldError(Exception):
    pass


class Board:
    def __init__(self):
        self._num_fields = NUMBER_FIELDS
        self._board = list(repeat(Field.EMPTY, self._num_fields))

        self._slices_rows = slice(None, 3), slice(3, 6), slice(6, None)
        self._slices_columns = slice(None, 7, 3), slice(1, 8, 3), slice(2, None, 3)
        self._slices_diagonals = slice(None, None, 4), slice(2, 7, 2)

    def __getitem__(self, index: int):
        self._check_range(index)

        return self._board[index]

    def __setitem__(self, index: int, field: Field):
        self._check_range(index)

        self._board[index] = field

    def _check_range(self, index: int):
        if index >= self._num_fields:
            raise NumFieldError(_('index param out of range'))

    @property
    def num_fields(self):
        return self._num_fields

    def fields(self) -> List[Any]:
        return [field for field in self._board]

    def rows(self) -> List[Any]:
        return [self._board[index] for index in self._slices_rows]

    def columns(self) -> List[Any]:
        return [self._board[index] for index in self._slices_columns]

    def diagonals(self) -> List[Any]:
        return [self._board[index] for index in self._slices_diagonals]

    def is_empty(self) -> bool:
        return all([x == Field.EMPTY for x in self._board])

    def field_is_empty(self, index: int) -> bool:
        self._check_range(index)

        return self._board[index] == Field.EMPTY

    def __len__(self) -> int:
        return self._num_fields

    def __str__(self) -> str:
        return str([(i, x) for i, x in enumerate(self._board)])
