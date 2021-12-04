"""Day 4: Giant Squid"""

from itertools import compress, chain, product


class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.bingo = False
        self.marks = [[1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1]]

    def mark(self, number):
        for row, col in product(range(5), repeat=2):
            if self.numbers[row][col] == number:
                self.marks[row][col] = 0
                self.check_bingo(row, col)

    def check_bingo(self, row, col):
        self.bingo |= sum(self.marks[row]) == 0 or \
                      sum(self.transpose(self.marks)[col]) == 0

    def transpose(self, matrix):
        return list(zip(*matrix))

    def flatten(self, matrix):
        return chain.from_iterable(matrix)

    def score(self):
        return sum(compress(self.flatten(self.numbers),
                            self.flatten(self.marks)))


def play_to_win(boards, draws):
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.bingo:
                return draw * board.score()

def play_to_loose(boards, draws):
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.bingo:
                boards = [b for b in boards if not b.bingo]
                if len(boards) == 0:
                    return draw * board.score()

def load_data(filename):
    with open(filename) as f:
        draws = [int(n) for n in f.readline().split(',')]
        boards = []
        while f.readline():
            boards.append(Board(
                [[int(n) for n in f.readline().split()] for _ in range(5)]))
    return boards, draws


if __name__ == '__main__':
    boards, draws = load_data('input.txt')
    print('part 1:', play_to_win(boards, draws))
    print('part 2:', play_to_loose(boards, draws))

