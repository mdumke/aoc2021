"""Day 4: Giant Squid"""

from itertools import chain, compress


class Matrix(list):
    @staticmethod
    def fill(fill_value, shape):
        return Matrix([[fill_value for _ in range(shape[1])]
                                   for _ in range(shape[0])])

    @property
    def shape(self):
        return len(self), len(self[0])

    def indices(self):
        return ((i, j) for i in range(len(self))
                       for j in range(len(self[0])))

    def flatten(self):
        return chain.from_iterable(self)

    def get_row(self, row):
        return self[row]

    def get_col(self, col):
        return list(zip(*self))[col]

    def find(self, value):
        for i, j in self.indices():
            if self[i][j] == value:
                return i, j


class Board(Matrix):
    def __init__(self, numbers):
        Matrix.__init__(self, numbers)
        self.bingo = False
        self.marks = Matrix.fill(1, shape=self.shape)

    def mark(self, number):
        if (pos := self.find(number)):
            self.marks[pos[0]][pos[1]] = 0
            self.check_bingo(pos[0], pos[1])

    def check_bingo(self, row, col):
        self.bingo |= sum(self.marks.get_row(row)) == 0 or \
                      sum(self.marks.get_col(col)) == 0

    def score(self):
        return sum(compress(self.flatten(), self.marks.flatten()))


def play(boards, draws, win=True):
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.bingo:
                if len(boards) == 1 or win:
                    return draw * board.score()
                boards = [b for b in boards if not b.bingo]
                continue


def load_data(filename):
    with open(filename) as f:
        draws = [int(n) for n in f.readline().split(',')]
        boards = []
        while f.readline():
            boards.append(
                [[int(n) for n in f.readline().split()] for _ in range(5)])
    return boards, draws


if __name__ == '__main__':
    boards, draws = load_data('input.txt')
    print('part 1:', play([Board(b) for b in boards], draws))
    print('part 2:', play([Board(b) for b in boards], draws, False))

