"""Day 24: Arithmetic Logic Unit"""

from functools import lru_cache

def find_model_number(program, find_largest=True):
    """returns the largest (or smallest) number the ALU will verify"""
    @lru_cache(None)
    def dfs_helper(op_index, w, x, y, z):
        if op_index >= len(program):
            return z == 0, []

        # we are looking for z=0,
        # prune the search tree at some point
        if z > 100_000_000:
            return False, None

        op, values = program[op_index]

        if op == 'inp':
            try_digits = range(9, 0, -1) if find_largest else range(1, 10)
            for digit in try_digits:
                success, digits = dfs_helper(op_index + 1, digit, x, y, z)
                if success:
                    return True, [digit, *digits]
            return False, None

        reg1, reg2 = values
        registers = dict(w=w, x=x, y=y, z=z)

        a = registers.get(reg1)
        b = registers.get(reg2) if reg2 in 'wxyz' else int(reg2)

        if op == 'add':
            registers[reg1] = a + b

        if op == 'mul':
            registers[reg1] = a * b

        if op == 'div':
            if b == 0:
                return False, None
            registers[reg1] = int(a / b)

        if op == 'mod':
            if a < 0 or b <= 0:
                return False, None
            registers[reg1] = a % b

        if op == 'eql':
            registers[reg1] = int(a == b)

        return dfs_helper(op_index + 1, *registers.values())

    return ''.join(map(str, dfs_helper(0, 0, 0, 0, 0)[1]))


if __name__ == '__main__':
    with open('input.txt') as f:
        program = [(l.split(' ')[0], l.split(' ')[1:]) for l in f.read().splitlines()]

    print('part 1:', find_model_number(program))
    print('part 2:', find_model_number(program, False))

