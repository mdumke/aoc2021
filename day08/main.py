"""Day 8: Seven Segment Search"""

def decode(entry):
    signal = sorted(entry[:10], key=len)
    one, seven, four, f1, f2, f3, s1, s2, s3, eight = signal
    three = [d for d in [f1, f2, f3] if len(set(d) & set(one)) == 2][0]
    two = [d for d in [f1, f2, f3] if len(set(d) & set(four)) == 2][0]
    five = [d for d in [f1, f2, f3] if d not in [two, three]][0]
    six = [d for d in [s1, s2, s3] if len(set(d) & set(one)) == 1][0]
    nine = [d for d in [s1, s2, s3] if len(set(d) & set(four)) == 4][0]
    zero = [d for d in [s1, s2, s3] if d not in [six, nine]][0]
    lookup = {k: i for i, k in enumerate(
        [zero, one, two, three, four, five, six, seven, eight, nine])}

    return int(''.join([str(lookup[d]) for d in entry[10:]]))


if __name__ == '__main__':
    with open('input.txt') as f:
         data = [line.replace('| ', '').split() for line in f.readlines()]
         data = [[''.join(sorted(d)) for d in entry] for entry in data]

    print('part 1:', sum(sum(len(digit) in [2, 3, 4, 7] for digit in entry[-4:]) for entry in data))
    print('part 2:', sum(decode(entry) for entry in data))
