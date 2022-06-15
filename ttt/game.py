import socket
from enum import Enum, auto, unique

from ttt.board import Board, Field


class QuitException(Exception):
    pass


@unique
class PlayerType(Enum):
    HUMAN = auto()
    COMPUTER = auto()


@unique
class StateGame(Enum):
    CONTINUES = auto()
    WIN_CROSS = auto()
    WIN_CIRCLE = auto()
    DRAW = auto()


class Player:
    def __init__(self, player: PlayerType, xo: Field, name: str = '') -> None:
        self._player = player
        self._type = xo

        if player == PlayerType.COMPUTER and not name:
            self._name = socket.gethostname()
        else:
            self._name = name

    @property
    def player(self) -> PlayerType:
        return self._player

    @property
    def type(self) -> Field:
        return self._type

    @property
    def xo(self) -> str:
        if self._type == Field.CROSS:
            return 'X'

        return 'O'

    @property
    def name(self) -> str:
        return self._name

    @property
    def ai(self) -> bool:
        return self._player == PlayerType.COMPUTER


class ConfigGame:
    player1 = PlayerType.HUMAN
    player2 = PlayerType.HUMAN
    debug = False


def state_game(board: Board) -> StateGame:
    circle = [Field.CIRCLE, Field.CIRCLE, Field.CIRCLE]
    cross = [Field.CROSS, Field.CROSS, Field.CROSS]

    for row in board.rows():
        if row == circle:
            return StateGame.WIN_CIRCLE
        elif row == cross:
            return StateGame.WIN_CROSS

    for column in board.columns():
        if column == circle:
            return StateGame.WIN_CIRCLE
        elif column == cross:
            return StateGame.WIN_CROSS

    for diagonal in board.diagonals():
        if diagonal == circle:
            return StateGame.WIN_CIRCLE
        elif diagonal == cross:
            return StateGame.WIN_CROSS

    for field in board.fields():
        if field == Field.EMPTY:
            return StateGame.CONTINUES

    return StateGame.DRAW


def display_board(board):
    for index, field in enumerate(board.fields(), 1):
        display = None

        if field == Field.EMPTY:
            display = str(index)
        elif field == Field.CROSS:
            display = 'X'
        elif field == Field.CIRCLE:
            display = 'O'
        else:
            continue

        print(f'[{display}]', end='')

        if index % 3 == 0:
            print()

    print()
