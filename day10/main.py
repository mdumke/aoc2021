"""Day 10: Syntax Scoring"""

def median(numbers):
    return sorted(numbers)[len(numbers) // 2]

def check_syntax(line):
    stack = []
    for char in line:
        if char in '({[<':
            stack.append(')]}>'['([{<'.index(char)])
        elif stack.pop() != char:
            return {'corrupted': char}
    return {'missing': reversed(stack)}

def score_helper(brackets):
    score = 0
    for v in [incomplete_value(b) for b in brackets]:
        score *= 5
        score += v
    return score

def corruption_value(bracket):
    return [3, 57, 1197, 25137][')}]>'.index(bracket)]

def incomplete_value(bracket):
    return [1, 2, 3, 4][')]}>'.index(bracket)]

def map_corrupted_chars(lines, fn):
    return [fn(c) for c in [check_syntax(l).get('corrupted') for l in lines] if c]

def map_missing_brackets(lines, fn):
    return [fn(b) for b in [check_syntax(l).get('missing') for l in lines] if b]

def compute_corruption_score(lines):
    return sum(map_corrupted_chars(lines, corruption_value))

def compute_incomplete_score(lines):
    return median(map_missing_brackets(lines, score_helper))


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    print('part 1:', compute_corruption_score(lines))
    print('part 2:', compute_incomplete_score(lines))

