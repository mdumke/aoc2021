"""Day 25: Sea Cucumber"""

def move_east(cucumbers):
    copy = [['.'] * len(cucumbers[0]) for _ in range(len(cucumbers))]
    changed = False
    for row in range(len(cucumbers)):
        for col in range(len(cucumbers[0])):
            next_col = (col + 1) % len(cucumbers[0])
            if cucumbers[row][col] == '>':
                if cucumbers[row][next_col] == '.':
                    copy[row][next_col] = '>'
                    changed = True
                else:
                    copy[row][col] = '>'
            elif cucumbers[row][col] == 'v':
                copy[row][col] = 'v'
    return copy, changed


def move_south(cucumbers):
    copy = [['.'] * len(cucumbers[0]) for _ in range(len(cucumbers))]
    changed = False
    for row in range(len(cucumbers)):
        for col in range(len(cucumbers[0])):
            next_row = (row + 1) % len(cucumbers)
            if cucumbers[row][col] == 'v':
                if cucumbers[next_row][col] == '.':
                    copy[next_row][col] = 'v'
                    changed = True
                else:
                    copy[row][col] = 'v'
            elif cucumbers[row][col] == '>':
                copy[row][col] = '>'
    return copy, changed


def find_halting_configuration(cucumbers):
    for i in range(10000):
        cucumbers, changed_east = move_east(cucumbers)
        cucumbers, changed_south = move_south(cucumbers)
        if not changed_east and not changed_south:
            return cucumbers, i + 1


if __name__ == '__main__':
    with open('input.txt') as f:
        cucumbers = [list(l) for l in f.read().splitlines()]

    print(find_halting_configuration(cucumbers)[1])

