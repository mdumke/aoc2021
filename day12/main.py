"""Day 12: Passage Pathing"""

from collections import defaultdict


def find_paths(caves, should_visit_twice=False):
    to_explore = [('start', [], False)]
    paths = []

    while len(to_explore):
        current, path, visited_twice = to_explore.pop()

        if current == 'end':
            paths.append([*path, current])
            continue

        if current.islower() and current in path:
            if not should_visit_twice or current == 'start' or visited_twice:
                continue
            visited_twice = True

        to_explore.extend(
            [(c, [*path, current], visited_twice) for c in caves[current]])

    return paths


def build_graph(edges):
    caves = defaultdict(list)
    for n1, n2 in edges:
        caves[n1].append(n2)
        caves[n2].append(n1)
    return caves


if __name__ == '__main__':
    with open('input.txt') as f:
        caves = build_graph([l.split('-') for l in f.read().splitlines()])

    print('part 1:', len(find_paths(caves)))
    print('part 2:', len(find_paths(caves, True)))

