"""Day 14: Extended Polymerization"""

from collections import defaultdict
from functools import reduce

def step(counts, rules):
    next_counts = defaultdict(int)
    for pair, count in counts.items():
        next_counts[pair[0] + rules[pair]] += count
        next_counts[rules[pair] + pair[1]] += count
    return next_counts

def iterate(counts, rules, steps):
    return reduce(lambda counts, _: step(counts, rules), range(steps), counts)

def get_char_counts(pair_counts):
    char_counts = defaultdict(int)
    for (char, _), pair_count in pair_counts.items():
        char_counts[char] += pair_count
    return char_counts

def count_pairs(template, rules):
    pairs = defaultdict(int)
    for a, b in list(zip(template, template[1:])):
        pairs[a + b] += 1
    return pairs

def get_element_counts(template, rules, n_iterations):
    counts = get_char_counts(iterate(count_pairs(template, rules), rules, n_iterations))
    counts[template[-1]] += 1
    return counts

def max_diff(counts):
    return max(counts.values()) - min(counts.values())


if __name__ == '__main__':
    with open('input.txt') as f:
        template, rules = f.read().split('\n\n')
        rules = dict((r[:2], r[-1]) for r in rules.splitlines())

    print('part 1:', max_diff(get_element_counts(template, rules, 10)))
    print('part 2:', max_diff(get_element_counts(template, rules, 40)))
