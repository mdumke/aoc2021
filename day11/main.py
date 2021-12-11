"""Day 11: Dumbo Octopus"""

def increment(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1

def get_flash_positions(grid):
    flash_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9:
                flash_positions.append((i, j))
    return flash_positions

def set_zeros(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] is None:
                grid[i][j] = 0

def is_flashable(grid, i, j):
    return i >= 0 and i < len(grid) and \
           j >= 0 and j < len(grid[0]) and \
           grid[i][j] is not None

def neighbors(grid, i, j):
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               ( 0, -1),          ( 0, 1),
               ( 1, -1), ( 1, 0), ( 1, 1)]
    return [(i+dx, j+dy) for dx, dy in offsets
                         if is_flashable(grid, i+dx, j+dy)]

def flash_at(grid, i, j):
    grid[i][j] = None
    new_positions = []
    for x, y in neighbors(grid, i, j):
        grid[x][y] += 1
        if grid[x][y] > 9:
            new_positions.append((x, y))
    return new_positions

def flash(grid):
    count = 0
    pos = get_flash_positions(grid)
    while len(pos):
        i, j = pos.pop()
        if grid[i][j] is not None:
            count += 1
            pos += flash_at(grid, i, j)
    set_zeros(grid)
    return count

def count_flashes(grid, steps):
    flash_count = 0
    for _ in range(steps):
        increment(grid)
        flash_count += flash(grid)
    return flash_count

def is_syncronized(grid):
    return sum(sum(row) for row in grid) == 0

def find_first_sync(grid):
    for i in range(100_000):
        increment(grid)
        flash(grid)
        if is_syncronized(grid):
            return i + 1

def load_grid(filename):
    with open(filename) as f:
        return [[int(n) for n in l] for l in f.read().splitlines()]


if __name__ == '__main__':
    print('part 1:', count_flashes(load_grid('input.txt'), 100))
    print('part 2:', find_first_sync(load_grid('input.txt')))
