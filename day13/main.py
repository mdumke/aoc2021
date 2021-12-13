"""Day 13: Transparent Origami"""

import re


def fold(axis, line, dots):
    res = set()
    for x, y in dots:
        if axis == 'x' and x > line:
            res.add((2 * line - x, y))
        elif axis == 'y' and y > line:
            res.add((x, 2 * line - y))
        else:
            res.add((x, y))
    return res

def fold_all(folds, dots):
    d = dots.copy()
    for axis, line in folds:
        d = fold(axis, line, d)
    return d

def display(dots):
    xs = [x for x, _ in dots]
    ys = [y for _, y in dots]
    screen = [[' '] * (max(xs) - min(xs) + 1)
              for _ in range(max(ys) - min(ys) + 1)]
    for x, y in dots:
        screen[y][x] = '#'
    return '\n'.join([''.join(line) for line in screen])

def load_instructions(filename):
    with open(filename) as f:
        dots, folds = f.read().split('\n\n')

    dots = set(tuple(int(n) for n in l.split(',')) for l in dots.splitlines())
    folds = [(c, int(n)) for c, n in re.findall(r'([xy])=(\d+)', folds)]

    return dots, folds


if __name__ == '__main__':
    dots, folds = load_instructions('input.txt')

    print('part 1:', len(fold(*folds[0], dots)))
    print('part 2:', '\n' + display(fold_all(folds, dots)))

