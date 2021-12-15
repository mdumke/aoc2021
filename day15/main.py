"""Day 15: Chiton"""

from heapq import heappush, heappop

def increment(grid):
    return [[(v % 9) + 1 for v in l] for l in grid]

def extend_right(grid1, grid2):
    return [l1 + l2 for l1, l2 in zip(grid1, increment(grid2))]

def extend_down(grid1, grid2):
    return grid1 + increment(grid2)

def extend_cave(c):
    c = extend_right(c, extend_right(c, extend_right(c, extend_right(c, c))))
    c = extend_down(c, extend_down(c, extend_down(c, extend_down(c, c))))
    return c

def get_neighbors(x, y, cave):
    return ((i, j) for (i, j) in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1))
                   if 0 <= i < len(cave) and 0 <= j < len(cave))

def find_lowest_risk(cave):
    fringe = [(0, (0, 0))]
    explored = set()

    while len(fringe):
        risk, (x, y) = heappop(fringe)

        if x == y == len(cave) - 1:
            return risk

        if (x, y) in explored:
            continue

        explored.add((x, y))

        for i, j in get_neighbors(x, y, cave):
            if (i, j) not in explored:
                heappush(fringe, (risk + cave[i][j], (i, j)))


if __name__ == '__main__':
    with open('input.txt') as f:
        cave = [[int(n) for n in l] for l in f.read().splitlines()]

    print('part 1:', find_lowest_risk(cave))
    print('part 2:', find_lowest_risk(extend_cave(cave)))


