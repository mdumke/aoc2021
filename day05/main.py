"""Day 5: Hydrothermal Venture"""

import re
from collections import defaultdict


def get_horizontal_coords(x1, x2, y):
    return [(i, y) for i in range(min(x1, x2), max(x1, x2) + 1)]

def get_vertical_coords(y1, y2, x):
    return [(x, i) for i in range(min(y1, y2), max(y1, y2) + 1)]

def get_diagonal_coords(x1, y1, x2, y2):
    h = 1 if x1 < x2 else -1
    v = 1 if y1 < y2 else -1
    return [(x1 + h * i, y1 + v * i) for i in range(abs(x2 - x1) + 1)]

def build_plan(lines, include_diagonals=False):
    plan = defaultdict(int)

    for x1, y1, x2, y2 in lines:
        if y1 == y2:
            for point in get_horizontal_coords(x1, x2, y1):
                plan[point] += 1
        elif x1 == x2:
            for point in get_vertical_coords(y1, y2, x1):
                plan[point] += 1
        elif include_diagonals:
            for point in get_diagonal_coords(x1, y1, x2, y2):
                plan[point] += 1

    return plan


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [[int(n) for n in re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', line)[0]]
                 for line in f.readlines()]

    print('part 1:', sum([count > 1 for count in build_plan(lines).values()]))
    print('part 2:', sum([count > 1 for count in build_plan(lines, True).values()]))

