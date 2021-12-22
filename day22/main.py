"""Day 22: Reactor Reboot"""

import re
from tqdm import tqdm
from dataclasses import dataclass
from itertools import chain


@dataclass
class Cube:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int
    on: bool = True

    @property
    def size(self):
        return (self.x2 - self.x1 + 1) * \
               (self.y2 - self.y1 + 1) * \
               (self.z2 - self.z1 + 1)

    def copy(self, **overrides):
        return Cuboid(**{**self.__dict__, **overrides})


def flatten(list_of_lists):
    """flatten one level of nesting"""
    return chain.from_iterable(list_of_lists)


def find_overlap(c1, c2) -> Cube:
    """returns the doubled cube if there is any overlap"""
    disjoint = c1.x2 < c2.x1 or c1.x1 > c2.x2 or \
               c1.y2 < c2.y1 or c1.y1 > c2.y2 or \
               c1.z2 < c2.z1 or c1.z1 > c2.z2

    if not disjoint:
        return Cube(
            max(c1.x1, c2.x1), min(c1.x2, c2.x2),
            max(c1.y1, c2.y1), min(c1.y2, c2.y2),
            max(c1.z1, c2.z1), min(c1.z2, c2.z2))


def shatter(cube, fixed):
    """break the cube and keep only pieces that do not overlap with fixed"""
    if not (overlap := find_overlap(cube, fixed)):
        return [cube]

    xs = [(max(cube.x1, fixed.x1), min(cube.x2, fixed.x2))]
    if cube.x1 < fixed.x1: xs.append((cube.x1, fixed.x1 - 1))
    if cube.x2 > fixed.x2: xs.append((fixed.x2 + 1, cube.x2))

    ys = [(max(cube.y1, fixed.y1), min(cube.y2, fixed.y2))]
    if cube.y1 < fixed.y1: ys.append((cube.y1, fixed.y1 - 1))
    if cube.y2 > fixed.y2: ys.append((fixed.y2 + 1, cube.y2))

    zs = [(max(cube.z1, fixed.z1), min(cube.z2, fixed.z2))]
    if cube.z1 < fixed.z1: zs.append((cube.z1, fixed.z1 - 1))
    if cube.z2 > fixed.z2: zs.append((fixed.z2 + 1, cube.z2))

    cubes = [Cube (*x, *y, *z) for x in xs for y in ys for z in zs]
    return [c for c in cubes if c != overlap]


def add(cube, active):
    """insert the cube into all cubes that are already active"""
    new_cubes = [cube]
    for fixed in active:
        new_cubes = flatten([shatter(c, fixed) for c in new_cubes])
    return [*active, *new_cubes]


def remove(cube, active):
    """discard the regions where the cube overlaps with activated cubes"""
    return list(flatten(shatter(c, cube) for c in active))


def is_small(cube):
    """returns true if the given cube is close to the center"""
    return cube.x1 >= -50 and cube.x2 <= 50 and \
           cube.y1 >= -50 and cube.y2 <= 50 and \
           cube.z1 >= -50 and cube.z2 <= 50


def reboot(steps):
    """returns a list of cubic regions that are activated"""
    active = [steps[0]]
    for cube in tqdm(steps[1:]):
        active = add(cube, active) if cube.on else remove(cube, active)
    return active


def count_status_on(cubes):
    """returns the total activate area"""
    return sum(cube.size for cube in cubes)


def parse(line):
    status, *values = re.findall(
        r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)',
        line)[0]
    return Cube(*[int(v) for v in values], status=='on')


if __name__ == '__main__':
    with open('input.txt') as f:
        steps = [parse(l) for l in f.read().splitlines()]
        small_steps = [s for s in steps if is_small(s)]

    print('part 1:', count_status_on(reboot(small_steps)))
    print('part 2:', count_status_on(reboot(steps)))

