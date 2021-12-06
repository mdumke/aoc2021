"""Lanternfish"""

from operator import countOf

def next_generation(p):
    """advances the given population by one day"""
    new_gen = [p[i] for i in range(1, 9)]
    new_gen[6] += p[0]
    new_gen.append(p[0])
    return new_gen

def get_population(fish, days):
    """returns the population after given days"""
    p = [countOf(fish, i) for i in range(9)]
    for _ in range(days):
        p = next_generation(p)
    return p


if __name__ == '__main__':
    with open('input.txt') as f:
        fish = [int(n) for n in f.read().split(',')]

    print('part 1:', sum(get_population(fish, 80)))
    print('part 2:', sum(get_population(fish, 256)))

