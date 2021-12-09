"""Day 9: Smoke Basin"""

from functools import reduce
from operator import mul

def neighbor_pos(cave, i, j):
    o = []
    if i > 0: o.append((i-1, j))
    if j > 0: o.append((i, j-1))
    if i < len(cave)-1: o.append((i+1, j))
    if j < len(cave[0])-1: o.append((i, j+1))
    return o

def is_low_point(cave, i, j):
    neighbors = [cave[x][y] for x, y in neighbor_pos(cave, i, j)]
    return all(height > cave[i][j] for height in neighbors)

def grow_basin(cave, i, j, basin):
    basin.add((i, j))
    for x, y in neighbor_pos(cave, i, j):
        if cave[x][y] > cave[i][j] and cave[x][y] < '9':
            grow_basin(cave, x, y, basin)
    return basin

def map_low_points(cave, fn):
    return [fn(i, j, int(cave[i][j]))
            for i in range(len(cave))
            for j in range(len(cave[0]))
            if is_low_point(cave, i, j)]

def get_total_risk_level(cave):
    return sum(map_low_points(cave, lambda i, j, h: 1 + h))

def get_basin_sizes(cave):
    return sorted(map_low_points(cave, lambda i, j, h: len(grow_basin(cave, i, j, set()))))


if __name__ == '__main__':
    with open('input.txt') as f:
        cave = f.read().splitlines()

    print('part 1:', get_total_risk_level(cave))
    print('part 2:', reduce(mul, get_basin_sizes(cave)[-3:]))
