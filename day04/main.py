"""Day 4: Giant Squid"""

from itertools import product
from copy import deepcopy

def mark(board, n):
    board = deepcopy(board)
    for i, j in product(range(5), repeat=2):
        if board[i][j] == n:
            board[5][5] -= n
            board[i][5] += 1
            board[5][j] += 1
            break
    return board

def is_bingo(board):
    for i in range(5):
        if board[i][5] == 5 or board[5][i] == 5:
            return True

def play(board, draws):
    for i, draw in enumerate(draws):
        board = mark(board, draw)
        if is_bingo(board):
            return i, draw * board[5][5]

def build_board(data):
    return [[*line, 0] for line in data] + \
           [[0, 0, 0, 0, 0, sum([sum(line) for line in data])]]

def load_data(filename):
    with open('input.txt') as f:
        draws, *board_data = f.read().split('\n\n')
    draws = [int(n) for n in draws.split(',')]
    board_data = [build_board([[int(n) for n in line.split()]
                           for line in b.strip().split('\n')])
                           for b in board_data]
    return draws, board_data


if __name__ == '__main__':
    draws, boards = load_data('input.txt')
    print('part 1:', min([play(board, draws) for board in boards])[1])
    print('part 2:', max([play(board, draws) for board in boards])[1])
