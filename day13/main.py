"""Day 13: Transparent Origami"""

import re
from functools import reduce

def matrix_to_str(m):
    return '\n'.join(''.join(row) for row in m)

def fold_coord(x, y, axis, line):
    return 2 * line - x if axis == 'x' and x > line else x, \
           2 * line - y if axis == 'y' and y > line else y

def fold(dots, instruction):
    return set(fold_coord(x, y, *instruction) for x, y in dots)

def get_axes(dots):
    return range(max(x for x, _ in dots) + 1), \
           range(max(y for _, y in dots) + 1)

def display(dots):
    return matrix_to_str([[' #'[(x, y) in dots]
                           for x in get_axes(dots)[0]]
                          for y in get_axes(dots)[1]])

def load_instructions(filename):
    with open(filename) as f:
        dots, folds = f.read().split('\n\n')

    dots = set(tuple(map(int, l.split(','))) for l in dots.splitlines())
    folds = [(ax, int(n)) for ax, n in re.findall(r'([xy])=(\d+)', folds)]

    return dots, folds


if __name__ == '__main__':
    dots, instructions = load_instructions('input.txt')
    print('part 1:', len(fold(dots, instructions[0])))
    print('part 2:\n', display(reduce(fold, instructions, dots)))

