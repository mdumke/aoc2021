"""Day 5: Hydrothermal Venture"""

from collections import namedtuple, defaultdict

Point = namedtuple('Point', 'x y')
Line = namedtuple('Line', 'p1 p2')

def get_horizontal_coords(line):
    l = min(line.p1.x, line.p2.x)
    r = max(line.p1.x, line.p2.x)
    return [Point(i, line.p1.y) for i in range(l, r+1)]

def get_vertical_coords(line):
    lo = min(line.p1.y, line.p2.y)
    hi = max(line.p1.y, line.p2.y)
    return [Point(line.p1.x, i) for i in range(lo, hi+1)]

def get_diagonal_coords(line):
    l = line.p1 if line.p1.x <= line.p2.x else line.p2
    r = line.p2 if l == line.p1 else line.p1
    slope = 1 if l.y < r.y else -1
    return [Point(l.x + i, l.y + slope * i) for i in range(r.x-l.x+1)]

def build_map(lines, include_diagonals=False):
    horizontals = [l for l in lines if l.p1.y == l.p2.y]
    verticals = [l for l in lines if l.p1.x == l.p2.x]
    diagonals = [l for l in lines if l.p1.x != l.p2.x and l.p1.y != l.p2.y]

    plan = defaultdict(int)

    for line in horizontals:
        for point in get_horizontal_coords(line):
            plan[point] += 1

    for line in verticals:
        for point in get_vertical_coords(line):
            plan[point] += 1

    if include_diagonals:
        for line in diagonals:
            for point in get_diagonal_coords(line):
                plan[point] += 1

    return plan

def parse_point(p):
    return Point(*[int(n) for n in p.split(',')])

def parse_line(raw):
    return Line(*[parse_point(p) for p in raw.strip().split(' -> ')])


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [parse_line(l) for l in f.readlines()]

    print('part 1:', sum([v > 1 for v in build_map(lines).values()]))
    print('part 2:', sum([v > 1 for v in build_map(lines, True).values()]))

