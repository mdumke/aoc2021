"""Day 17: Trick Shot"""

from collections import namedtuple

Area = namedtuple('Area', 'x1 y1 x2 y2')

def fire(vx, vy, target):
    x, y = 0, 0
    max_y = -10_000
    i = 0
    while True:
        x = x + vx
        y = y + vy
        max_y = max(y, max_y)
        vx = 0 if vx == 0 else vx - 1
        vy -= 1
        if target.x1 <= x <= target.x2 and \
           target.y2 <= y <= target.y1:
            return 'hit', max_y, i
        if vx == 0 and x < target.x1:
            return 'undershoot-x', max_y, i
        if x > target.x2:
            return 'overshoot-x', max_y, i
        if vx == 0 and y < target.y2:
            return 'overshoot-y', max_y, i
        i += 1

def find_hit_velocities(target):
    hits = []
    for vy in range(-100, 100):
        vx = 1
        while True:
            response, max_y, i = fire(vx, vy, target)
            if response == 'hit':
                hits.append((max_y, vx, vy))
            if response == 'overshoot-x' and i == 0:
                break
            vx += 1
    return hits


if __name__ == '__main__':
    target = Area(236, -58, 262, -78)
    hits = sorted(find_hit_velocities(target))

    print('part 1:', hits[-1][0])
    print('part 2:', len(hits))
