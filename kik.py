#!python3

import timeit

import ttt.lang as lang
from ttt.ai import find_best_move
from ttt.board import Board, Field
from ttt.game import (ConfigGame, Player, PlayerType, QuitException, StateGame,
                      display_board, state_game)

_ = lang.i18n.t

__version__ = '1.2'


def banner():
    print(_('kik.version') + ':', __version__)
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
    return input(_('kik.enter_name') % {'number': number, 'symbol': symbol} + ': ')


def enter_number(string: str):
    while True:
        choice = input(string)

        try:
            choice = int(choice)
            break
        except ValueError:
            print('\n' + _('kik.enter_number_err'))
            continue

    return choice


def menu():
    options = (0, 1, 2, 3)
    print(_('kik.pvp'))
    print(_('kik.pvc'))
    print(_('kik.cvc'))
    print(_('kik.quit'))
    print()

    while True:
        number = enter_number(_('kik.select_game') + ': ')

        if number not in options:
            print(_('kik.bad_number'))
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
        print(_('kik.farewell'))
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
            choice = enter_number(_('kik.select_field') % {'name': current_player.name} + ': ')

            if not 1 <= choice <= 9:
                print(_('kik.enter_number'))
                continue

            if board[choice - 1] != Field.EMPTY:
                print(_('kik.field_occupied') % {'number': choice})
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

            print(_('kik.ai_select') % {'name': current_player.name, 'xo': current_player.xo, 'choice': choice})

            config.debug and print(f'Time of turn {turn}:', timeit.default_timer() - start)

        board[choice - 1] = current_player.type
        display_board(board)
        state = state_game(board)

        config.debug and print(f'State game: {state}')

        if state == StateGame.WIN_CROSS:
            print(_('kik.cross_won'))
            break
        elif state == StateGame.WIN_CIRCLE:
            print(_('kik.circle_won'))
            break
        elif state == StateGame.DRAW:
            print(_('kik.draw'))
            break

        turn += 1

    config.debug and print('Ran et', timeit.default_timer() - run)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n' + _('kik.quit_text'))
