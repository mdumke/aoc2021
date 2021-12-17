"""Day 17: Trick Shot"""

from dataclasses import dataclass

@dataclass
class Area:
    x1: int
    y1: int
    x2: int
    y2: int

    def contains(self, x, y):
        return self.x1 <= x <= self.x2 and \
               self.y2 <= y <= self.y1

    def missed(self, x, y):
        return x > self.x2 or y < self.y2


def fire(vx, vy, target):
    top = -10000
    x, y = 0, 0

    for i in range(10000):
        x = x + vx
        y = y + vy
        top = max(y, top)
        vx = max(0, vx - 1)
        vy -= 1

        if target.contains(x, y):
            return 'hit', top

        if target.missed(x, y):
            return 'pass' if i == 0 else 'miss', top


def find_hit_velocities(target):
    hits = []

    for vy in range(-100, 100):
        for vx in range(1, 10000):
            response, max_y = fire(vx, vy, target)

            if response == 'hit':
                hits.append(max_y)

            if response == 'pass':
                break

    return hits


if __name__ == '__main__':
    hits = sorted(find_hit_velocities(Area(236, -58, 262, -78)))

    print('part 1:', hits[-1])
    print('part 2:', len(hits))
