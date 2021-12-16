"""Packet Decoder"""

import math
from operator import gt, lt

def hex_to_bin(n):
    return ''.join([str(bin(int(i, base=16)))[2:].rjust(4, '0') for i in n])

def decode_literal(bits):
    lit = ''
    i = 0
    while True:
        lit += bits[i+1:i+5]
        i += 5
        if bits[i-5] == '0':
            break
    return int(lit, 2), i

def decode_packet(bits):
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)

    global version_sum
    version_sum += version

    if type_id == 4:
        n, offset = decode_literal(bits[6:])
        return n, offset + 6
    else:
        ns, offset = decode_packet_list(bits[6:])

        if type_id == 0:
            result = sum(ns)
        if type_id == 1:
            result = math.prod(ns)
        if type_id == 2:
            result = min(ns)
        if type_id == 3:
            result = max(ns)
        if type_id == 5:
            result = gt(*ns)
        if type_id == 6:
            result = lt(*ns)
        if type_id == 7:
            result = ns[0] == ns[1]

        return result, 6 + offset

def decode_packet_list(bits):
    if int(bits[0], 2) == 0:
        length = int(bits[1:16], 2)
        ns, offset = decode_sequence(bits[16:16+length])
        return ns, 16 + offset
    else:
        n_sub = int(bits[1:12], 2)
        ns, offset = decode_group(bits[12:], n_sub)
        return ns, 12 + offset

def decode_sequence(bits):
    values = []
    i = 0
    while i < len(bits):
        v, offset = decode_packet(bits[i:])
        i += offset
        values.append(v)
    return values, i

def decode_group(bits, size):
    i = 0
    values = []
    for packet in range(size):
        v, offset = decode_packet(bits[i:])
        i += offset
        values.append(v)
    return values, i


if __name__ == '__main__':
    with open('input.txt') as f:
        bits = hex_to_bin(f.readline().strip())

    version_sum = 0
    result = decode_packet(bits)[0]

    print('part 1:', version_sum)
    print('part 2:', result)

