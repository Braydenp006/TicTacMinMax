"""
Tic Tac Toe Player
"""

import math
import copy

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
    Counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                Counter += 1

    if board == initial_state():
        return X
    
    if Counter % 2 == 1:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                a.add((i, j))

    return a

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("oops")
        
    newboard = copy.deepcopy(board)
    if player(board) == X:
        newboard[action[0]][action[1]] = X
    elif player(board) == O:
        newboard[action[0]][action[1]] = O
    
    return newboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
    
    if board[0][0] == board [1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    EmptyCount = 0
    if winner(board) == X or winner(board) == O:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
                EmptyCount += 1
    
    if EmptyCount == 0:
        return True
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    Max = -9999
    Min = 9999
    if terminal(board) == True:
        return None
    if player(board) == X:
        return MaxValue(board, Max, Min)[1];
    else:
        return MinValue(board, Max, Min)[1];
    
def MaxValue(board, Max, Min):

    action = None
    if terminal(board):
        return[utility(board), None];
    v = -9999
    for a in actions(board):
        print(a)
        print(Max)
        Test = MinValue(result(board, a), Max, Min)[0];
        print(Test, "test")
        Max = max(Max, Test)
        if Test > v:
            v = Test
            action = a
        if Max >= Min:
            break
    return [v, action];

def MinValue(board, Max, Min):

    action = None
    if terminal(board):
        return[utility(board), None];
    v = 9999
    for a in actions(board):
        print(a)
        print(Max)
        Test = MaxValue(result(board, a), Max, Min)[0];
        print(Test, "test")
        Min = min(Min, Test)
        if Test < v:
            v = Test
            action = a
        if Min <= Max:
            break
    return [v, action];

    