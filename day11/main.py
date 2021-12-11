"""Day 11: Dumbo Octopus"""

def size(grid):
    return len(grid) * len(grid[0])

def positions(grid):
    return ((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def find(value, grid):
    return ((i, j) for i, j in positions(grid) if grid[i][j] == value)

def count(value, grid):
    return len(list(find(value, grid)))

def replace(v1, v2, grid):
    for i, j in find(v1, grid):
        grid[i][j] = v2

def increment_at(positions, grid):
    for i, j in positions:
        grid[i][j] += 1

def is_valid(i, j, grid):
    return i >= 0 and i < len(grid) and \
           j >= 0 and j < len(grid[0]) and \
           grid[i][j] is not None

def get_neighbors(i, j, grid):
    return filter(lambda pos: is_valid(*pos, grid),
                 ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1),
                  (i+1, j-1), (i+1, j), (i+1, j+1)))

def should_flash(positions, grid):
    return set((i, j) for i, j in positions if grid[i][j] > 9)

def flash(grid):
    to_flash = should_flash(positions(grid), grid)
    while len(to_flash):
        i, j = to_flash.pop()
        grid[i][j] = None
        increment_at(get_neighbors(i, j, grid), grid)
        to_flash.update(should_flash(get_neighbors(i, j, grid), grid))

def step(grid):
    increment_at(positions(grid), grid)
    flash(grid)
    replace(None, 0, grid)

def count_flashes(grid, steps):
    flash_count = 0
    for _ in range(steps):
        step(grid)
        flash_count += count(0, grid)
    return flash_count

def find_first_sync(grid):
    for n in range(1, 10000):
        step(grid)
        if count(0, grid) == size(grid):
            return n

def load_grid(filename):
    with open(filename) as f:
        return [[int(n) for n in l] for l in f.read().splitlines()]


if __name__ == '__main__':
    print('part 1:', count_flashes(load_grid('input.txt'), 100))
    print('part 2:', find_first_sync(load_grid('input.txt')))
