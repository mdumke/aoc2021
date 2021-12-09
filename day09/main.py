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


def get_total_risk_level(cave):
    return sum(1 + int(cave[i][j])
               for i in range(len(cave))
               for j in range(len(cave[0]))
               if is_low_point(cave, i, j))

def grow_basin(cave, i, j, basin):
    """returns points in the area that are higher than cave(i, j)"""
    if cave[i][j] == '9':
        return basin
    basin.add((i, j))
    for x, y in neighbor_pos(cave, i, j):
        if cave[x][y] > cave[i][j]:
            grow_basin(cave, x, y, basin)
    return basin

def get_basin_sizes(cave):
    sizes = [len(grow_basin(cave, i, j, set()))
             for i in range(len(cave))
             for j in range(len(cave[0]))
             if is_low_point(cave, i, j)]
    return sorted(sizes, reverse=True)


if __name__ == '__main__':
    with open('input.txt') as f:
        cave = f.read().splitlines()

    print('part 1:', get_total_risk_level(cave))
    print('part 2:', reduce(mul, get_basin_sizes(cave)[:3]))
