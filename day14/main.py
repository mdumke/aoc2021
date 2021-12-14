"""Day 14: Extended Polymerization"""

from collections import defaultdict

def step(counts, rules):
    next_counts = defaultdict(int)

    for pair, count in counts.items():
        if rules.get(pair):
            next_counts[pair[0] + rules[pair]] += count
            next_counts[rules[pair] + pair[1]] += count
        else:
            next_counts[pair] = 1

    return next_counts

def iterate(counts, rules, steps):
    c = counts.copy()
    for _ in range(steps):
        c = step(c, rules)
    return c

def get_char_counts(counts):
    char_counts = defaultdict(int)
    for (a, _), count in counts.items():
        if a != ' ':
            char_counts[a] += count
    return char_counts

def max_diff(counts):
    return sorted(counts.values())[-1] - \
           sorted(counts.values())[0]


if __name__ == '__main__':
    with open('input.txt') as f:
        template, rules = f.read().split('\n\n')
        rules = dict((r[:2], r[-1]) for r in rules.splitlines())

    counts = dict.fromkeys(rules.keys(), 0)
    for a, b in list(zip(template, template[1:])):
        counts[a + b] += 1

    counts[' ' + template[0]] = 1
    counts[template[-1] + ' '] = 1

    print('part 1:', max_diff(get_char_counts(iterate(counts, rules, 10))))
    print('part 2:', max_diff(get_char_counts(iterate(counts, rules, 40))))
