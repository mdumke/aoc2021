"""Day 18: Snailfish"""

from math import floor, ceil
from functools import reduce
from itertools import permutations

def find_mid(s):
    depth = 0
    for i, char in enumerate(s):
        if char == '[': depth += 1
        if char == ']': depth -= 1
        if char == ',' and depth == 1:
            return i

def parse(s):
    if s[0] in '0123456789':
        return int(s[0])
    mid = find_mid(s)
    return parse(s[1:mid]), \
           parse(s[mid+1:])

def insert_left(n, i):
    return n + i if isinstance(n, int) else (insert_left(n[0], i), n[1])

def insert_right(n, i):
    return n + i if isinstance(n, int) else (n[0], insert_right(n[1], i))

def explode(n, depth=1):
    if depth == 4:
        if isinstance(n[0], tuple):
            return (0, insert_left(n[1], n[0][1])), (n[0][0], 0)

        if isinstance(n[1], tuple):
            return (insert_right(n[0], n[1][0]), 0), (0, n[1][1])

        return n, None

    if isinstance(n[0], tuple):
        update, insert = explode(n[0], depth + 1)
        if insert:
            return (update, insert_left(n[1], insert[1])), (insert[0], 0)

    if isinstance(n[1], tuple):
        update, insert = explode(n[1], depth + 1)
        if insert:
            return (insert_right(n[0], insert[0]), update), (0, insert[1])

    return n, None

def split(n):
    if isinstance(n, int):
        if n < 10:
            return n, False
        else:
            return (floor(n/2), ceil(n/2)), True
    left, updated = split(n[0])
    if updated:
        return (left, n[1]), True
    right, updated = split(n[1])
    if updated:
        return (n[0], right), True
    return n, False


def add(n1, n2):
    n = (n1, n2)
    while True:
        n, changed = explode(n)
        if changed:
            continue
        n, changed = split(n)
        if not changed:
            return n


def magnitude(n):
    return n if isinstance(n, int) else 3 * magnitude(n[0]) + 2 * magnitude(n[1])


def pair_magnitudes(n):
    return [magnitude(add(*pair)) for pair in permutations(numbers, 2)]


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = [parse(l) for l in f.read().splitlines()]

    print('part 1:', magnitude(reduce(add, numbers)))
    print('part 2:', sorted(pair_magnitudes(numbers))[-1])

