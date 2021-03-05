import unittest

from board import Board, Field
from game import StateGame, state_game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_1_state_game_win_first_row(self):
        '''Win crosses or circles in first row.
        set fields of board 1:
          [X][X][X]
          [O][ ][ ]
          [O][ ][ ]

        set fields of board 2:
          [O][O][O]
          [X][ ][ ]
          [X][ ][ ]
        '''
        self.board[0] = Field.CROSS
        self.board[1] = Field.CROSS
        self.board[2] = Field.CROSS
        self.board[3] = Field.CIRCLE
        self.board[6] = Field.CIRCLE

        self.assertEqual(state_game(self.board), StateGame.WIN_CROSS)

        self.board[0] = Field.CIRCLE
        self.board[1] = Field.CIRCLE
        self.board[2] = Field.CIRCLE
        self.board[3] = Field.CROSS
        self.board[6] = Field.CROSS

        self.assertEqual(state_game(self.board), StateGame.WIN_CIRCLE)

    def test_2_state_game_win_second_row(self):
        '''Win crosses or cirlces in second row.
        set fields of board 1:
          [ ][ ][ ]
          [X][X][X]
          [O][O][ ]

         set fields of board 2:
           [ ][ ][ ]
           [O][O][O]
           [X][X][ ]
        '''
        self.board[3] = Field.CROSS
        self.board[4] = Field.CROSS
        self.board[5] = Field.CROSS
        self.board[6] = Field.CIRCLE
        self.board[7] = Field.CIRCLE

        self.assertEqual(state_game(self.board), StateGame.WIN_CROSS)

        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CIRCLE
        self.board[5] = Field.CIRCLE
        self.board[6] = Field.CROSS
        self.board[7] = Field.CROSS

        self.assertEqual(state_game(self.board), StateGame.WIN_CIRCLE)

    def test_3_state_game_win_third_row(self):
        '''Win crosses or circles in third row.
        set fields of board 1:
          [O][ ][ ]
          [ ][O][ ]
          [X][X][X]

        set fields of board 2:
          [X][ ][ ]
          [ ][X][ ]
          [O][O][O]
        '''
        self.board[0] = Field.CIRCLE
        self.board[4] = Field.CIRCLE
        self.board[6] = Field.CROSS
        self.board[7] = Field.CROSS
        self.board[8] = Field.CROSS

        self.assertEqual(state_game(self.board), StateGame.WIN_CROSS)

        self.board[0] = Field.CROSS
        self.board[4] = Field.CROSS
        self.board[6] = Field.CIRCLE
        self.board[7] = Field.CIRCLE
        self.board[8] = Field.CIRCLE

        self.assertEqual(state_game(self.board), StateGame.WIN_CIRCLE)

    def test_4_state_game_win_first_column(self):
        '''Win crosses or circles in first column.
        set fields of board 1:
          [X][O][ ]
          [X][O][ ]
          [X][ ][ ]

        set fields of board 2:
          [O][X][ ]
          [O][X][ ]
          [O][ ][ ]

        '''
        self.board[0] = Field.CROSS
        self.board[1] = Field.CIRCLE
        self.board[3] = Field.CROSS
        self.board[4] = Field.CIRCLE
        self.board[6] = Field.CROSS

        self.assertEqual(state_game(self.board), StateGame.WIN_CROSS)

        self.board[0] = Field.CIRCLE
        self.board[1] = Field.CROSS
        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CROSS
        self.board[6] = Field.CIRCLE

        self.assertEqual(state_game(self.board), StateGame.WIN_CIRCLE)


    def test_5_state_game_win_second_column(self):
        '''Win crosses or circles in second column.
        set fields of board 1:
          [O][X][ ]
          [ ][X][ ]
          [ ][X][O]

        set fields of board 2:
          [X][O][ ]
          [ ][O][ ]
          [ ][O][X]

        '''
        self.board[0] = Field.CIRCLE
        self.board[1] = Field.CROSS
        self.board[4] = Field.CROSS
        self.board[7] = Field.CROSS
        self.board[8] = Field.CIRCLE

        self.assertEqual(state_game(self.board), StateGame.WIN_CROSS)

        self.board[0] = Field.CROSS
        self.board[1] = Field.CIRCLE
        self.board[4] = Field.CIRCLE
        self.board[7] = Field.CIRCLE
        self.board[8] = Field.CROSS

        self.assertEqual(state_game(self.board), StateGame.WIN_CIRCLE)

    def test_6_state_game_win_third_column(self):
        '''Win crosses or circles in third column.
        set fields of board 1:
          [O][ ][X]
          [ ][O][X]
          [ ][ ][X]

        set fields of board 2:
          [X][ ][O]
          [ ][X][O]
          [ ][ ][O]

        '''
        self.board[0] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[4] = Field.CIRCLE
        self.board[5] = Field.CROSS
        self.board[8] = Field.CROSS

        self.assertEqual(state_game(self.board), StateGame.WIN_CROSS)

        self.board[0] = Field.CROSS
        self.board[2] = Field.CIRCLE
        self.board[4] = Field.CROSS
        self.board[5] = Field.CIRCLE
        self.board[8] = Field.CIRCLE

        self.assertEqual(state_game(self.board), StateGame.WIN_CIRCLE)

    def test_7_state_game_win_first_diagonal(self):
        '''Win crosses or circles in first diagonal.
        set fields of board 1:
          [X][ ][ ]
          [O][X][O]
          [ ][ ][X]

        set fields of board 2:
          [O][ ][ ]
          [X][O][X]
          [ ][ ][O]

        '''
        self.board[0] = Field.CROSS
        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CROSS
        self.board[5] = Field.CIRCLE
        self.board[8] = Field.CROSS

        self.assertEqual(state_game(self.board), StateGame.WIN_CROSS)

        self.board[0] = Field.CIRCLE
        self.board[3] = Field.CROSS
        self.board[4] = Field.CIRCLE
        self.board[5] = Field.CROSS
        self.board[8] = Field.CIRCLE

        self.assertEqual(state_game(self.board), StateGame.WIN_CIRCLE)

    def test_8_state_game_win_second_diagonal(self):
        '''Win crosses or circles in second diagonal.
        set fields of board 1:
          [O][ ][X]
          [ ][X][ ]
          [X][ ][O]

        set fields of board 2:
          [X][ ][O]
          [ ][O][ ]
          [O][ ][X]

        '''
        self.board[0] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[4] = Field.CROSS
        self.board[6] = Field.CROSS
        self.board[8] = Field.CIRCLE

        self.assertEqual(state_game(self.board), StateGame.WIN_CROSS)

        self.board[0] = Field.CROSS
        self.board[2] = Field.CIRCLE
        self.board[4] = Field.CIRCLE
        self.board[6] = Field.CIRCLE
        self.board[8] = Field.CROSS

        self.assertEqual(state_game(self.board), StateGame.WIN_CIRCLE)

    def test_9_state_game_continues(self):
        '''Continues game.
        set fields of board (finish):
          [X][X][O]
          [O][O][X]
          [X][O][X]
        '''
        self.board[0] = Field.CROSS
        self.assertEqual(state_game(self.board), StateGame.CONTINUES)

        self.board[1] = Field.CROSS
        self.assertEqual(state_game(self.board), StateGame.CONTINUES)

        self.board[2] = Field.CIRCLE
        self.assertEqual(state_game(self.board), StateGame.CONTINUES)

        self.board[3] = Field.CIRCLE
        self.assertEqual(state_game(self.board), StateGame.CONTINUES)

        self.board[4] = Field.CIRCLE
        self.assertEqual(state_game(self.board), StateGame.CONTINUES)

        self.board[5] = Field.CROSS
        self.assertEqual(state_game(self.board), StateGame.CONTINUES)

        self.board[6] = Field.CROSS
        self.assertEqual(state_game(self.board), StateGame.CONTINUES)

        self.board[7] = Field.CIRCLE
        self.assertEqual(state_game(self.board), StateGame.CONTINUES)

        self.board[8] = Field.CROSS
        self.assertNotEqual(state_game(self.board), StateGame.CONTINUES)

    def test_10_state_game_draw(self):
        '''Draw game.
        set fields of board:
          [X][X][O]
          [O][O][X]
          [X][O][X]
        '''
        self.board[0] = Field.CROSS
        self.board[1] = Field.CROSS
        self.board[2] = Field.CIRCLE
        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CIRCLE
        self.board[5] = Field.CROSS
        self.board[6] = Field.CROSS
        self.board[7] = Field.CIRCLE
        self.board[8] = Field.CROSS

        self.assertEqual(state_game(self.board), StateGame.DRAW)


if __name__ == '__main__':
    unittest.main()
