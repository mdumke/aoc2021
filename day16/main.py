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
        lit, offset = decode_literal(bits[6:])
        return None, offset + 6
    elif int(bits[6], 2) == 0:
        length = int(bits[7:22], 2)
        _, offset = decode_sequence(bits[22:22+length])
        return None, 22 + offset
    else:
        n_sub = int(bits[7:18], 2)
        _, offset = decode_group(bits[18:], n_sub)
        return None, 18 + offset

def decode_sequence(bits):
    i = 0
    while i < len(bits):
        _, offset = decode_packet(bits[i:])
        i += offset
    return None, i

def decode_group(bits, size):
    i = 0
    for packet in range(size):
        res, offset = decode_packet(bits[i:])
        i += offset
    return None, i


if __name__ == '__main__':
    with open('input.txt') as f:
        msg = f.readline().strip()

    bits = hex_to_bin(msg)
    version_sum = 0
    decode_packet(bits)
    print(version_sum)
