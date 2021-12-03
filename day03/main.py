"""Day 3: Binary Diagnostic"""

def gamma(report):
    return bin2dec(column_map(report, arg_max))

def epsilon(report):
    return bin2dec(column_map(report, arg_min))

def oxygen(report):
    return bin2dec(filter_down(report, arg_max))

def co2(report):
    return bin2dec(filter_down(report, arg_min))

def arg_max(bits):
    return int(sum(bits) >= len(bits) / 2)

def arg_min(bits):
    return int(sum(bits) < len(bits) / 2)

def bin2dec(bit_list):
    return int(''.join(map(str, bit_list)), base=2)

def transpose(matrix):
    return list(zip(*matrix))

def column_map(report, fn):
    return [fn(col) for col in transpose(report)]

def filter_down(report, criterion):
    rest = report
    for i in range(len(report)):
        bit = criterion(transpose(rest)[i])
        rest = [r for r in rest if r[i] == bit]
        if len(rest) <= 1:
            return rest[0]


if __name__ == '__main__':
    with open('input.txt') as f:
        report = [[int(c) for c in list(l.strip())] for l in f.readlines()]

    print('part 1:', gamma(report) * epsilon(report))
    print('part 2:', oxygen(report) * co2(report))

