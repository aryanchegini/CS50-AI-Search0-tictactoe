"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for section in row:
            if section == EMPTY:
                count += 1

    if count % 2 == 0:
        return O
    elif count % 2 == 1:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resulting_board = copy.deepcopy(board)
    if resulting_board[action[0]][action[1]] == EMPTY:
        resulting_board[action[0]][action[1]] = player(resulting_board)
    elif resulting_board[action[0]][action[1]] != EMPTY:
        raise Exception("This is not a legal move")
    return resulting_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    ways_to_win = {
        "row1": [(0, 0), (0, 1), (0, 2)],
        "row2": [(1, 0), (1, 1), (1, 2)],
        "row3": [(2, 0), (2, 1), (2, 2)],
        "column1": [(0, 0), (1, 0), (2, 0)],
        "column2": [(0, 1), (1, 1), (2, 1)],
        "column3": [(0, 2), (1, 2), (2, 2)],
        "diagonal1": [(0, 0), (1, 1), (2, 2)],
        "diagonal2": [(2, 0), (1, 1), (0, 2)]
    }

    for way in ways_to_win:
        x = 0
        o = 0
        for section in ways_to_win[way]:
            if board[section[0]][section[1]] == X:
                x += 1
            elif board[section[0]][section[1]] == O:
                o += 1

        if x == 3:
            return X
        elif o == 3:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    count = 0
    for row in board:
        for section in row:
            if section == EMPTY:
                count += 1

    if winner(board) is not None:
        return True
    elif count == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board), None

    v_0 = -math.inf
    optimal_move = None
    for action in actions(board):
        v_1, move = min_value(result(board, action))
        if v_1 > v_0:
            optimal_move = action
        v_0 = max(v_0, v_1)
    return v_0, optimal_move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v_0 = math.inf
    optimal_move = None
    for action in actions(board):
        v_1, move = max_value(result(board, action))
        if v_1 < v_0:
            optimal_move = action
        v_0 = min(v_0, v_1)
    return v_0, optimal_move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        v, optimal_move = max_value(board)
        return optimal_move
    elif player(board) == O:
        v, optimal_move = min_value(board)
        return optimal_move
