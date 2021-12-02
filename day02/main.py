"""Day 2: Dive!"""

def solve_part1(commands):
    x, depth = 0, 0
    for d, n in commands:
        if d == 'up': depth -= n
        if d == 'down': depth += n
        if d == 'forward': x += n
    return x * depth

def solve_part2(commands):
    x, depth, aim = 0, 0, 0
    for d, n in commands:
        if d == 'up': aim -= n
        if d == 'down': aim += n
        if d == 'forward':
            x += n
            depth += n * aim
    return x * depth


if __name__ == '__main__':
    with open('input.txt') as f:
        commands = [(d, int(n)) for d, n in [l.split() for l in f.readlines()]]

    print('part 1:', solve_part1(commands))
    print('part 2:', solve_part2(commands))
