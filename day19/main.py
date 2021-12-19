"""Day 19: Beacon Scanner"""

import numpy as np
from itertools import combinations


def readings_as_set(data):
    return set(tuple(row) for row in data)


def transformers():
    rot = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    bases = [np.diag([1, 1, 1]), np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])]
    for matrix in bases:
        for _ in range(3):
            for j in range(4):
                yield matrix
                matrix = rot @ matrix
            matrix = np.vstack([matrix[1:], matrix[0]])


def adjust_scanner(scanner1, scanner2):
    target_set = set(tuple(row) for row in scanner1.tolist())

    for tf in transformers():
        scanner2_tf = scanner2 @ tf

        for target in scanner1:
            for candidate in scanner2_tf:
                candidate_set = readings_as_set(scanner2_tf + target - candidate)

                overlap = target_set & candidate_set

                if len(overlap) >= 12:
                    return scanner2_tf + target - candidate, target - candidate


def adjust(scanners):
    beacons = readings_as_set(scanners[0])
    offsets = [np.array([0, 0, 0])]

    newly_adjusted_scanners = [scanners[0]]
    open_scanners = scanners[1:]

    while newly_adjusted_scanners:
        base = newly_adjusted_scanners.pop()

        check_again = []
        for scanner in open_scanners:
            adjustments = adjust_scanner(base, scanner)

            if adjustments is not None:
                readings, offset = adjustments
                newly_adjusted_scanners.append(readings)
                beacons.update(readings_as_set(readings))
                offsets.append(offset)
            else:
                check_again.append(scanner)

        open_scanners = check_again
        print('unadjusted scanners:', len(open_scanners))

    return beacons, offsets


def max_dist(points):
    def manhattan(p1, p2):
        return sum([abs(i - j) for i, j in zip(p1, p2)])

    return max([manhattan(p1, p2) for p1, p2 in combinations(points, 2)])


def parse(inpt):
    return np.array([[int(n) for n in line.split(',')] for line in inpt[1:]])


if __name__ == '__main__':
    with open('input.txt') as f:
        scanners = [parse(line.splitlines()) for line in f.read().split('\n\n')]

    beacons, offsets = adjust(scanners)
    print('part 1:', len(beacons))
    print('part 2:', max_dist(offsets))

