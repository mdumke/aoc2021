"""Day 23: Amphipod"""

from itertools import product
from heapq import heappush, heappop

class Burrow:
    expected_types = {2: 'A', 4: 'B', 6: 'C', 8: 'D'}
    home_columns = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
    energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

    def __init__(self, amphis, depth=2, cost=0):
        self.amphis = amphis
        self.depth = depth
        self.cost = cost
        self.hash = self.compute_hash()

    def complete(self):
        """returns True if all rooms are locked with X"""
        return all(typ == 'X' for typ in self.amphis.values())

    def mark_fixed(self):
        """set amphis to X that are already in target position"""
        for room in self.rooms():
            for row, col in reversed(room):
                if not (typ := self.amphis.get((row, col))):
                    break

                if typ == 'X':
                    continue

                if typ == Burrow.expected_types[col]:
                    self.amphis[(row, col)] = 'X'
                else:
                    break

    def neighbors(self):
        """returns possible burrows that can be reached in one move"""
        return [*self.moves_out(), *self.moves_in()]

    def moves_out(self):
        """returns all moves from any room to the floor"""
        neighbors = []
        for room in self.rooms():
            for row, col in room:
                if not (typ := self.amphis.get((row, col))):
                    continue

                if typ != 'X':
                    neighbors.extend(self.trace_outwards(row, col))

                break

        return neighbors

    def moves_in(self):
        """returns all moves from the floor to a room"""
        neighbors = []
        for col in range(0, 11):
            if not self.occupied(0, col):
                continue

            if (neighbor := self.trace_inwards(col)):
                neighbors.append(neighbor)

        return neighbors

    def trace_outwards(self, row, col):
        """returns moves from a given room to the floor"""
        neighbors = []

        target_col = col - 1
        while not self.occupied(0, target_col) and target_col >= 0:
            if target_col not in Burrow.expected_types.keys():
                neighbors.append(self.get_neighbor(row, col, 0, target_col))
            target_col -= 1

        target_col = col + 1
        while not self.occupied(0, target_col) and target_col <= 10:
            if target_col not in Burrow.expected_types.keys():
                neighbors.append(self.get_neighbor(row, col, 0, target_col))
            target_col += 1

        return neighbors

    def trace_inwards(self, col):
        """returns a move from the given floor position to the room if possible"""
        typ = self.amphis.get((0, col))
        target_col = Burrow.home_columns[typ]
        direction = 1 if col < target_col else -1
        col_cursor = col + direction
        while col_cursor != target_col:
            if self.occupied(0, col_cursor):
                return None
            col_cursor += direction

        row_cursor = 1
        while row_cursor < self.depth:
            if self.occupied(row_cursor, target_col):
                return None

            if not self.occupied(row_cursor + 1, target_col):
                row_cursor += 1
                continue

            if self.amphis.get((row_cursor + 1, target_col)) not in [typ, 'X']:
                return None

            break

        return self.get_neighbor(0, col, row_cursor, target_col, fixed=True)


    def get_neighbor(self, row, col, target_row, target_col, fixed=False):
        """returns the burrow reached by moving from source to target position"""
        new_amphis = {pos: typ for pos, typ in self.amphis.items() if pos != (row, col)}
        new_amphis[(target_row, target_col)] = 'X' if fixed else self.amphis[(row, col)]
        new_cost = self.compute_cost(row, col, target_row, target_col)
        return Burrow(new_amphis, self.depth, new_cost)


    def compute_cost(self, row, col, target_row, target_col):
        """returns the enery required to perform the given move"""
        return self.cost + (abs(row - target_row) + abs(col - target_col)) * \
                self.get_energy_level(row, col)


    def get_energy_level(self, row, col):
        """returns the enery level of the amphi at the given position"""
        return Burrow.energy.get(self.amphis.get((row, col)))


    def rooms(self):
        """returns coordinates of rooms"""
        return ([(row, col) for row in range(1, self.depth + 1)]
                for col in Burrow.expected_types.keys())

    def occupied(self, row, col):
        """returns true if an amphi is at the given position"""
        return self.amphis.get((row, col)) is not None


    def __lt__(self, other):
        return self.cost < other.cost

    def compute_hash(self):
        return hash(str(self))

    def __repr__(self):
        matrix = [[0] * 11 for _ in range(self.depth+1)]
        for (row, col), typ in self.amphis.items():
            matrix[row][col] = typ
        return '\n'.join([' '.join(map(str, row)) for row in matrix]).replace('0', '.')


def find_least_reorder_energy(burrow):
    fringe = [burrow]
    seen = set()

    while len(fringe):
        current = heappop(fringe)

        if current.complete():
            return current.cost

        if current.hash in seen:
            continue

        seen.add(current.hash)

        for neighbor in current.neighbors():
            if neighbor.hash not in seen:
                heappush(fringe, neighbor)


def parse_input(setup):
    return {(row, col-1): setup[row][col] for row, col in product(range(1, len(setup)), (3, 5, 7, 9))}


if __name__ == '__main__':
    with open('input.txt') as f:
        base = f.read().splitlines()[1:-1]
        extended = base[:2] + ['  #D#C#B#A#  ', '  #D#B#A#C#  '] + base[-1:]

    burrow = Burrow(parse_input(base))
    burrow.mark_fixed()
    print('part 1:', find_least_reorder_energy(burrow))

    burrow = Burrow(parse_input(extended), depth=4)
    burrow.mark_fixed()
    print('part 2:', find_least_reorder_energy(burrow))


