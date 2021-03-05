#!python3

import gettext
import timeit

from ai import find_best_move
from board import Board, Field
from game import ConfigGame, Player, PlayerType, QuitException, StateGame, display_board, state_game

gettext.bindtextdomain('kik', 'locale')
gettext.textdomain('kik')
_ = gettext.gettext

__version__ = '1.0'


def banner():
    print(_('Tic Tac Toe version:'), __version__)
    print(r'''
         .     .--.     .
       .'|     |__|   .'|
     .'  |     .--. .'  |
    <    |     |  |<    |
     |   | ____|  | |   | ____
     |   | \ .'|  | |   | \ .'
     |   |/  . |  | |   |/  .
     |    /\  \|__| |    /\  \
     |   |  \  \    |   |  \  \
     '    \  \  \   '    \  \  \
    '------'  '---''------'  '---'
Generate: http://www.patorjk.com/software/taag/
''')


def configure(player1: PlayerType = None, player2: PlayerType = None, debug: bool = False) -> ConfigGame:
    config = ConfigGame()

    if player1:
        config.player1 = player1

    if player2:
        config.player2 = player2

    config.debug = debug

    return config


def enter_name(number: int, symbol: str) -> str:
    return input(_('Player {} [{}] - enter your name: ').format(number, symbol))


def enter_number(string: str):
    while True:
        choice = input(string)

        try:
            choice = int(choice)
            break
        except ValueError:
            print('\n', _('Enter number!'))
            continue

    return choice


def menu():
    options = (0, 1, 2, 3)
    print(_('1 - player vs player'))
    print(_('2 - player vs computer'))
    print(_('3 - computer vs computer'))
    print(_('0 - quit'))
    print()

    while True:
        number = enter_number(_('Select the game type: '))

        if number not in options:
            print(_('Bad number, enter again!'))
            continue

        if number == 1:
            return configure(PlayerType.HUMAN, PlayerType.HUMAN)
        elif number == 2:
            return configure(PlayerType.HUMAN, PlayerType.COMPUTER)
        elif number == 3:
            return configure(PlayerType.COMPUTER, PlayerType.COMPUTER)
        elif number == 0:
            raise QuitException


def main():
    banner()
    player1_name = None
    player2_name = None

    try:
        config = menu()
    except QuitException:
        print(_('Bye, bye...'))
        return

    if config.player1 == PlayerType.HUMAN:
        player1_name = enter_name(1, 'X')

    if config.player2 == PlayerType.HUMAN:
        player2_name = enter_name(2, 'O')

    player1 = Player(config.player1, Field.CROSS, player1_name)
    player2 = Player(config.player2, Field.CIRCLE, player2_name)
    board = Board()
    choice = None
    current_player = player1
    turn = 0

    if config.debug:
        run = timeit.default_timer()

    display_board(board)

    while True:
        if turn % 2 == 0:
            current_player = player1
        else:
            current_player = player2

        while True and not current_player.ai:
            choice = enter_number(_('{} choice field number [1-9]: ').format(current_player.name))

            if choice < 1 or choice > 9:
                print(_('Enter number from 1 to 9!'))
                continue

            if board[choice - 1] != Field.EMPTY:
                print(_('Field number {} is not empty.').format(choice))
                continue

            break

        if current_player.ai:
            if config.debug:
                start = timeit.default_timer()

            if current_player is player1:
                opponent = player2
            else:
                opponent = player1

            choice = find_best_move(board, current_player.type, opponent.type) + 1

            print(f'{current_player.name} {current_player.xo}: choice {choice}')

            config.debug and print(f'Time of turn {turn}:', timeit.default_timer() - start)

        board[choice - 1] = current_player.type
        display_board(board)
        state = state_game(board)

        config.debug and print(f'State game: {state}')

        if state == StateGame.WIN_CROSS:
            print(_('Crosses won.'))
            break
        elif state == StateGame.WIN_CIRCLE:
            print(_('Circles won.'))
            break
        elif state == StateGame.DRAW:
            print(_('Draw.'))
            break

        turn += 1

    config.debug and print('Ran et', timeit.default_timer() - run)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n', _('See you later!'))
