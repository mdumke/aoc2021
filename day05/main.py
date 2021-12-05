"""Day 5: Hydrothermal Venture"""

from collections import namedtuple, defaultdict

Point = namedtuple('Point', 'x y')

def get_horizontal_coords(p1, p2):
    l, r = (p1, p2) if p1.x <= p2.x else (p2, p1)
    return [(i, l.y) for i in range(l.x, r.x+1)]

def get_vertical_coords(p1, p2):
    lo, hi = (p1, p2) if p1.y <= p2.y else (p2, p1)
    return [(lo.x, i) for i in range(lo.y, hi.y+1)]

def get_diagonal_coords(p1, p2):
    l, r = (p1, p2) if p1.x <= p2.x else (p2, p1)
    slope = 1 if l.y < r.y else -1
    return [(l.x + i, l.y + slope * i) for i in range(r.x-l.x+1)]

def build_map(lines, include_diagonals=False):
    horizontals = [(p1, p2) for p1, p2 in lines if p1.y == p2.y]
    verticals = [(p1, p2) for p1, p2 in lines if p1.x == p2.x]
    diagonals = [(p1, p2) for p1, p2 in lines if p1.x != p2.x and p1.y != p2.y]

    plan = defaultdict(int)

    for line in horizontals:
        for point in get_horizontal_coords(*line):
            plan[point] += 1

    for line in verticals:
        for point in get_vertical_coords(*line):
            plan[point] += 1

    if include_diagonals:
        for line in diagonals:
            for point in get_diagonal_coords(*line):
                plan[point] += 1

    return plan


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [[Point(*[int(n) for n in p.split(',')])
                  for p in line.strip().split(' -> ')]
                 for line in f.readlines()]

    print('part 1:', sum([v > 1 for v in build_map(lines).values()]))
    print('part 2:', sum([v > 1 for v in build_map(lines, True).values()]))

