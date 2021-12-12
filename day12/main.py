"""Day 12: Passage Pathing"""

def find_paths(caves, without_repetition=True):
    paths = []
    fringe = [('start', [], without_repetition)]

    while len(fringe):
        cave, path, free_visit_complete = fringe.pop()

        if cave == 'end':
            paths.append([*path, cave])
            continue

        if cave.islower() and cave in path and free_visit_complete:
            continue

        if cave.islower() and cave in path:
            free_visit_complete = True

        for neighbor in caves[cave]:
            if neighbor != 'start':
                fringe.append([neighbor, [*path, cave], free_visit_complete])

    return paths

def load_cave_plan(filename):
    with open(filename) as f:
        edges = [l.split('-') for l in f.read().splitlines()]

    caves = {}

    for n1, n2 in edges:
        if not caves.get(n1): caves[n1] = []
        if not caves.get(n2): caves[n2] = []
        caves[n1].append(n2)
        caves[n2].append(n1)

    return caves


if __name__ == '__main__':
    caves = load_cave_plan('input.txt')
    print('part 1:', len(find_paths(caves)))
    print('part 2:', len(find_paths(caves, False)))

