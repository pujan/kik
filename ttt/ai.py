from ttt.board import Board, Field
from ttt.game import StateGame, state_game


def evaluate(board: Board, player: Field, opponent: Field) -> int:
    # checking rows
    for row in board.rows():
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] == player:
                return 10
            elif row[0] == opponent:
                return -10

    # checking columns
    for column in board.columns():
        if column[0] == column[1] and column[1] == column[2]:
            if column[0] == player:
                return 10
            elif column[0] == opponent:
                return -10

    # checking diagonals
    for diagonal in board.diagonals():
        if diagonal[0] == diagonal[1] and diagonal[1] == diagonal[2]:
            if diagonal[0] == player:
                return 10
            elif diagonal[0] == opponent:
                return -10

    return 0


def moves_left(board: Board) -> bool:
    return state_game(board) == StateGame.CONTINUES


def minimax(board: Board, player: Field, opponent: Field, depth: int, is_max: bool) -> int:
    scores = evaluate(board, player, opponent)

    if scores == 10 or scores == -10:
        return scores

    scores = 0

    if not moves_left(board):
        return scores

    if is_max:
        best = -1000

        for index, field in enumerate(board.fields()):
            if field == Field.EMPTY:
                # Make the move player
                board[index] = player

                # call minimax recursively
                best = max(best, minimax(board, player, opponent, depth + 1, not is_max))

                # Undo the move
                board[index] = field

        return best
    else:
        best = 1000

        for index, field in enumerate(board.fields()):
            if field == Field.EMPTY:
                # Make the move opponent
                board[index] = opponent

                # call minimax recursively
                best = min(best, minimax(board, player, opponent, depth + 1, not is_max))

                # Undo the move
                board[index] = field

        return best


def find_best_move(board: Board, player: Field, opponent: Field) -> int:
    best_score = -1000
    best_field = -1

    for index, field in enumerate(board.fields()):
        if field == Field.EMPTY:
            # Make the move
            board[index] = player

            move_score = minimax(board, player, opponent, 0, False)

            # Undo the move
            board[index] = field

            if move_score > best_score:
                best_score = move_score
                best_field = index

    # print('BEST Score:', best_score)
    # print('BEST Move:', best_field)

    return best_field
