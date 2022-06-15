import unittest

from ttt.ai import evaluate, find_best_move, minimax
from ttt.board import Board, Field


class TestAI(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_evaluate_win_in_first_column(self):
        '''Win player in first column.
        set fields of board:
            [X][O][X]
            [X][O][O]
            [X][ ][ ]
        '''
        # first row
        self.board[0] = Field.CROSS
        self.board[1] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[3] = Field.CROSS
        self.board[4] = Field.CIRCLE
        self.board[5] = Field.CIRCLE
        self.board[6] = Field.CROSS

        self.assertEqual(evaluate(self.board, player=Field.CROSS, opponent=Field.CIRCLE), 10)
        self.assertEqual(evaluate(self.board, player=Field.CIRCLE, opponent=Field.CROSS), -10)

    def test_evaluate_win_in_second_column(self):
        '''Win player in second column.
        set fields of board:
            [O][O][X]
            [X][O][X]
            [ ][O][ ]
        '''
        self.board[0] = Field.CIRCLE
        self.board[1] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[3] = Field.CROSS
        self.board[4] = Field.CIRCLE
        self.board[5] = Field.CROSS
        self.board[7] = Field.CIRCLE

        self.assertEqual(evaluate(self.board, player=Field.CIRCLE, opponent=Field.CROSS), 10)
        self.assertEqual(evaluate(self.board, player=Field.CROSS, opponent=Field.CIRCLE), -10)

    def test_evaluate_win_in_third_column(self):
        '''Win player in third column.
        set fields of board:
            [X][O][X]
            [O][O][X]
            [ ][ ][X]
        '''
        self.board[0] = Field.CIRCLE
        self.board[1] = Field.CROSS
        self.board[2] = Field.CROSS
        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CIRCLE
        self.board[5] = Field.CROSS
        self.board[8] = Field.CROSS

        self.assertEqual(evaluate(self.board, player=Field.CROSS, opponent=Field.CIRCLE), 10)
        self.assertEqual(evaluate(self.board, player=Field.CIRCLE, opponent=Field.CROSS), -10)

    def test_evaluate_win_in_first_row(self):
        '''Win player in first row.
        set fields of board:
            [O][O][O]
            [O][X][X]
            [X][ ][ ]
        '''
        self.board[0] = Field.CIRCLE
        self.board[1] = Field.CIRCLE
        self.board[2] = Field.CIRCLE
        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CROSS
        self.board[5] = Field.CROSS
        self.board[6] = Field.CROSS

        self.assertEqual(evaluate(self.board, player=Field.CIRCLE, opponent=Field.CROSS), 10)
        self.assertEqual(evaluate(self.board, player=Field.CROSS, opponent=Field.CIRCLE), -10)

    def test_evaluate_win_in_second_row(self):
        '''Win player in second row.
        set fields of board:
          [O][O][X]
          [X][X][X]
          [ ][O][ ]
        '''
        self.board[0] = Field.CIRCLE
        self.board[1] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[3] = Field.CROSS
        self.board[4] = Field.CROSS
        self.board[5] = Field.CROSS
        self.board[7] = Field.CIRCLE

        self.assertEqual(evaluate(self.board, player=Field.CROSS, opponent=Field.CIRCLE), 10)
        self.assertEqual(evaluate(self.board, player=Field.CIRCLE, opponent=Field.CROSS), -10)

    def test_evaluate_win_in_third_row(self):
        '''Win player in third row.
        set fields of board:
           [O][X][ ]
           [X][X][ ]
           [O][O][O]
        '''
        self.board[0] = Field.CIRCLE
        self.board[1] = Field.CROSS
        self.board[3] = Field.CROSS
        self.board[4] = Field.CROSS
        self.board[6] = Field.CIRCLE
        self.board[7] = Field.CIRCLE
        self.board[8] = Field.CIRCLE

        self.assertEqual(evaluate(self.board, player=Field.CIRCLE, opponent=Field.CROSS), 10)
        self.assertEqual(evaluate(self.board, player=Field.CROSS, opponent=Field.CIRCLE), -10)

    def test_evaluate_empty_board(self):
        '''Evaluate empty board.
        set fields of board:
          [ ][ ][ ]
          [ ][ ][ ]
          [ ][ ][ ]
        '''
        self.assertEqual(evaluate(self.board, player=Field.CIRCLE, opponent=Field.CROSS), 0)
        self.assertEqual(evaluate(self.board, player=Field.CROSS, opponent=Field.CIRCLE), 0)

    def test_evaluate_not_win_and_not_draw(self):
        '''Evaluate not win game and not draw game - continue game.
        set fields of board:
          [X][ ][ ]
          [ ][O][ ]
          [ ][ ][ ]
        '''
        self.board[0] = Field.CROSS
        self.board[4] = Field.CIRCLE

        self.assertEqual(evaluate(self.board, player=Field.CIRCLE, opponent=Field.CROSS), 0)
        self.assertEqual(evaluate(self.board, player=Field.CROSS, opponent=Field.CIRCLE), 0)

    def test_evaluate_draw_game(self):
        '''Evauate draw game.
        set fields of board:
          [X][O][X]
          [O][X][X]
          [O][X][O]
        '''
        self.board[0] = Field.CROSS
        self.board[1] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CROSS
        self.board[5] = Field.CROSS
        self.board[6] = Field.CIRCLE
        self.board[7] = Field.CROSS
        self.board[8] = Field.CIRCLE

        self.assertEqual(evaluate(self.board, player=Field.CIRCLE, opponent=Field.CROSS), 0)
        self.assertEqual(evaluate(self.board, player=Field.CROSS, opponent=Field.CIRCLE), 0)

    def test_minimax_empty_board(self):
        '''Minimax scores for X and O for empty board.
        set fields of board:
          [ ][ ][ ]
          [ ][ ][ ]
          [ ][ ][ ]
        '''
        self.assertEqual(minimax(self.board, Field.CROSS, Field.CIRCLE, 0, False), 0)
        self.assertEqual(minimax(self.board, Field.CROSS, Field.CIRCLE, 0, True), 0)

    def test_minimax_draw_game(self):
        '''Minimax scores for X and O for draw game - not empty field.
        set fields of board:
          [X][O][X]
          [O][X][X]
          [O][X][O]
        '''
        self.board[0] = Field.CROSS
        self.board[1] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CROSS
        self.board[5] = Field.CROSS
        self.board[6] = Field.CIRCLE
        self.board[7] = Field.CROSS
        self.board[8] = Field.CIRCLE

        self.assertEqual(minimax(self.board, Field.CROSS, Field.CIRCLE, 0, False), 0)
        self.assertEqual(minimax(self.board, Field.CROSS, Field.CIRCLE, 0, True), 0)

    def test_minimax_win(self):
        '''Minimax scores for X and O for win X or O.
        set fields of board:
          [O][ ][X]
          [O][X][ ]
          [ ][ ][O]
        '''
        self.board[0] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CROSS
        self.board[8] = Field.CIRCLE

        self.assertEqual(minimax(self.board, Field.CIRCLE, Field.CROSS, 0, False), -10)
        self.assertEqual(minimax(self.board, Field.CIRCLE, Field.CROSS, 0, True), 10)

    def test_minimax_not_win(self):
        '''Minimax scores for X and O - third move.
        set fields of board:
          [O][ ][ ]
          [ ][X][ ]
          [ ][ ][ ]
        '''
        self.board[0] = Field.CIRCLE
        self.board[4] = Field.CROSS

        self.assertEqual(minimax(self.board, Field.CROSS, Field.CIRCLE, 0, False), 0)
        self.assertEqual(minimax(self.board, Field.CROSS, Field.CIRCLE, 0, True), 0)

    def test_find_best_move_start(self):
        '''Find the best move of start game.
        set fields of board:
          [ ][ ][ ]
          [ ][ ][ ]
          [ ][ ][ ]
        '''
        self.assertEqual(find_best_move(self.board, Field.CROSS, Field.CIRCLE), 0)
        self.assertEqual(find_best_move(self.board, Field.CIRCLE, Field.CROSS), 0)

    def test_find_best_move_half(self):
        '''Find the best move of half game.
        set fields of board:
          [O][ ][X]
          [O][X][ ]
          [ ][ ][ ]
        '''
        self.board[0] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CROSS

        self.assertEqual(find_best_move(self.board, Field.CROSS, Field.CIRCLE), 6)
        self.assertEqual(find_best_move(self.board, Field.CIRCLE, Field.CROSS), 6)

    def test_find_best_move_half_2(self):
        '''Find the best move of half game.
        set fields of board:
          [O][ ][O]
          [ ][X][X]
          [X][O][ ]
        '''
        self.board[0] = Field.CIRCLE
        self.board[2] = Field.CIRCLE
        self.board[4] = Field.CROSS
        self.board[5] = Field.CROSS
        self.board[6] = Field.CROSS
        self.board[7] = Field.CIRCLE

        self.assertEqual(find_best_move(self.board, Field.CROSS, Field.CIRCLE), 3)
        self.assertEqual(find_best_move(self.board, Field.CIRCLE, Field.CROSS), 1)
