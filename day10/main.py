"""Day 10: Syntax Scoring"""

complements = {'(': ')', '[': ']', '{': '}', '<': '>'}
corruption_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_scores ={')': 1, ']': 2, '}': 3, '>': 4}

def check_syntax(line):
    stack = []
    for char in line:
        if char in complements:
            stack.append(char)
        else:
            bracket = stack.pop()

            if char != complements[bracket]:
                return char, None
    return None, stack

def compute_corruption_score(lines):
    total = 0
    for line in lines:
        char, stack = check_syntax(line)
        if char:
            total += corruption_scores[char]
    return total

def score_helper(stack):
    score = 0
    while len(stack):
        score *= 5
        score += incomplete_scores[complements[stack.pop()]]
    return score

def compute_incomplete_score(lines):
    scores = []
    for line in lines:
        char, stack = check_syntax(line)
        if char is None:
            scores.append(score_helper(stack))
    return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()

    print('part 1:', compute_corruption_score(lines))
    print('part 2:', compute_incomplete_score(lines))

