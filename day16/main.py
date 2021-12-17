"""Packet Decoder"""

from math import prod

def hex_to_bin(msg):
    return ''.join(str(bin(int(n, base=16)))[2:].rjust(4, '0') for n in msg)

def decode_literal(bits):
    lit = ''
    for i in range(0, len(bits), 5):
        lit += bits[i+1:i+5]
        if bits[i] == '0':
            return int(lit, 2), i + 5

def decode_packet(bits):
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)

    global version_sum
    version_sum += version

    if type_id == 4:
        result, offset = decode_literal(bits[6:])
    else:
        ns, offset = decode_packet_list(bits[6:])
        if type_id == 0: result = sum(ns)
        if type_id == 1: result = prod(ns)
        if type_id == 2: result = min(ns)
        if type_id == 3: result = max(ns)
        if type_id == 5: result = ns[0] > ns[1]
        if type_id == 6: result = ns[0] < ns[1]
        if type_id == 7: result = ns[0] == ns[1]
    return result, 6 + offset

def decode_packet_list(bits):
    if int(bits[0], 2) == 0:
        length = int(bits[1:16], 2)
        ns, offset = decode_sequence(bits[16:16+length])
        return ns, 16 + offset
    else:
        n_sub = int(bits[1:12], 2)
        ns, offset = decode_sequence(bits[12:], n_sub)
        return ns, 12 + offset

def decode_sequence(bits, size=None):
    values = []
    offset = 0
    packet = 0
    while offset < len(bits) if size is None else packet < size:
        v, i = decode_packet(bits[offset:])
        offset += i
        packet += 1
        values.append(v)
    return values, offset


if __name__ == '__main__':
    with open('input.txt') as f:
        bits = hex_to_bin(f.readline().strip())

    version_sum = 0
    result = decode_packet(bits)[0]

    print('part 1:', version_sum)
    print('part 2:', result)

