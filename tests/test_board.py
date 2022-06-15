import unittest

from ttt.board import NUMBER_FIELDS, Board, Field


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_1_rows(self):
        """Rows.
        [X][X][X]
        [O][O][O]
        [ ][ ][ ]
        """
        self.board[0] = Field.CROSS
        self.board[1] = Field.CROSS
        self.board[2] = Field.CROSS

        self.board[3] = Field.CIRCLE
        self.board[4] = Field.CIRCLE
        self.board[5] = Field.CIRCLE

        board = self.board.rows()

        self.assertEqual(board[0], [Field.CROSS, Field.CROSS, Field.CROSS])
        self.assertEqual(board[1], [Field.CIRCLE, Field.CIRCLE, Field.CIRCLE])
        self.assertEqual(board[2], [Field.EMPTY, Field.EMPTY, Field.EMPTY])

    def test_2_columns(self):
        """Columns.
        [X][O][ ]
        [X][O][ ]
        [X][O][ ]
        """
        self.board[0] = Field.CROSS
        self.board[3] = Field.CROSS
        self.board[6] = Field.CROSS

        self.board[1] = Field.CIRCLE
        self.board[4] = Field.CIRCLE
        self.board[7] = Field.CIRCLE

        board = list(self.board.columns())

        self.assertEqual(board[0], [Field.CROSS, Field.CROSS, Field.CROSS])
        self.assertEqual(board[1], [Field.CIRCLE, Field.CIRCLE, Field.CIRCLE])
        self.assertEqual(board[2], [Field.EMPTY, Field.EMPTY, Field.EMPTY])

    def test_3_diagonals(self):
        """Diagonals.
        [X][ ][X]
        [ ][X][ ]
        [O][ ][O]
        """
        self.board[0] = Field.CROSS
        self.board[8] = Field.CIRCLE

        self.board[4] = Field.CROSS

        self.board[2] = Field.CROSS
        self.board[6] = Field.CIRCLE

        board = self.board.diagonals()

        self.assertEqual(board[0], [Field.CROSS, Field.CROSS, Field.CIRCLE])
        self.assertEqual(board[1], [Field.CROSS, Field.CROSS, Field.CIRCLE])

    def test_4_num_fields(self):
        '''Test number fields property.'''
        self.assertEqual(self.board.num_fields, NUMBER_FIELDS)

    def test_5_is_empty(self):
        '''Test if empty or not empty.'''
        self.assertEqual(self.board.is_empty(), True)

        self.board[4] = Field.CIRCLE

        self.assertEqual(self.board.is_empty(), False)

    def test_6_field_is_empty(self):
        '''Test fieds is empty or not empty.
        set fields of board:
          [X][O][X]
          [ ][O][ ]
          [ ][ ][ ]
        '''
        self.board[0] = Field.CROSS
        self.board[1] = Field.CIRCLE
        self.board[2] = Field.CROSS
        self.board[4] = Field.CIRCLE

        self.assertEqual(self.board.field_is_empty(0), False)
        self.assertEqual(self.board.field_is_empty(1), False)
        self.assertEqual(self.board.field_is_empty(2), False)
        self.assertEqual(self.board.field_is_empty(3), True)
        self.assertEqual(self.board.field_is_empty(4), False)
        self.assertEqual(self.board.field_is_empty(5), True)
        self.assertEqual(self.board.field_is_empty(6), True)
        self.assertEqual(self.board.field_is_empty(7), True)
        self.assertEqual(self.board.field_is_empty(8), True)


if __name__ == '__main__':
    unittest.main()
