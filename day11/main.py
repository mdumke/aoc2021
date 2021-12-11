"""Day 11: Dumbo Octopus"""

def positions(grid):
    return ((i, j) for i in range(len(grid))
                   for j in range(len(grid[0])))

def sum2d(grid):
    return sum(sum(row) for row in grid)

def count(grid, value):
    return sum(1 for i, j in positions(grid) if grid[i][j] == value)

def increment(grid):
    for i, j in positions(grid):
        grid[i][j] += 1

def flash_positions(grid):
    return [(i, j) for i, j in positions(grid) if grid[i][j] > 9]

def set_zeros(grid):
    for i, j in positions(grid):
        if grid[i][j] is None:
            grid[i][j] = 0

def is_valid(grid, i, j):
    return i >= 0 and i < len(grid) and \
           j >= 0 and j < len(grid[0]) and \
           grid[i][j] is not None

def neighbors(grid, i, j):
    return filter(lambda pos: is_valid(grid, *pos),
                 ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1),
                  (i+1, j-1), (i+1, j), (i+1, j+1)))

def flash_at(grid, i, j):
    grid[i][j] = None
    for x, y in neighbors(grid, i, j):
        grid[x][y] += 1
    return [(x, y) for x, y in neighbors(grid, i, j) if grid[x][y] > 9]

def flash(grid):
    pos = flash_positions(grid)
    while len(pos):
        i, j = pos.pop()
        if grid[i][j] is not None:
            pos += flash_at(grid, i, j)

def step(grid):
    increment(grid)
    flash(grid)
    set_zeros(grid)
    return count(grid, 0)

def count_flashes(grid, steps):
    return sum(step(grid) for _ in range(steps))

def find_first_sync(grid):
    for n in range(1, 10000):
        step(grid)
        if sum2d(grid) == 0:
            return n

def load_grid(filename):
    with open(filename) as f:
        return [[int(n) for n in l] for l in f.read().splitlines()]


if __name__ == '__main__':
    print('part 1:', count_flashes(load_grid('input.txt'), 100))
    print('part 2:', find_first_sync(load_grid('input.txt')))
