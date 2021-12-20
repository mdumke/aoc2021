"""Day 20: Trench Map"""

def enhance(algorithm):
    return lambda window: algorithm[int(''.join(window), 2)]

def valid_index(i, j, matrix):
    return 0 <= i < len(matrix) and \
           0 <= j < len(matrix[0])

def get_window(img, i, j, fill_value):
    return [''.join([img[x][y] if valid_index(x, y, img) else fill_value
             for y in (j-1, j, j+1)])
            for x in (i-1, i, i+1)]

def convolve(img, fill_value, fn):
    return [''.join(fn(get_window(img, i, j, fill_value))
             for j in range(-1, len(img) + 1))
            for i in range(-1, len(img[0]) + 1)]

def enhance_image(img, n, enhancer):
    fill = '0'
    for _ in range(n):
        img = convolve(img, fill, enhancer)
        fill = algorithm[int(fill * 9, 2)]
    return img


if __name__ == '__main__':
    with open('input.txt') as f:
        algorithm = f.readline().strip().replace('#', '1').replace('.', '0')
        img = [l.replace('#', '1').replace('.', '0') for l in f.read().strip().splitlines()]

    print('part 1:', ''.join(enhance_image(img, 2, enhance(algorithm))).count('1'))
    print('part 2:', ''.join(enhance_image(img, 50, enhance(algorithm))).count('1'))

