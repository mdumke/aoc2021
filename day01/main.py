"""Day 1: Sonar Sweep"""

def sliding_window(values, size, fn):
    return [fn(tup) for tup in zip(*[values[i:] for i in range(size)])]

def count_increases(numbers):
    return sum(sliding_window(numbers, 2, lambda t: t[0] < t[1]))


if __name__ == '__main__':
    with open('input.txt') as f:
        values = [int(n) for n in f.readlines()]

    print('part 1:', count_increases(values))
    print('part 2:', count_increases(sliding_window(values, 3, sum)))
