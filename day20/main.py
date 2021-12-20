"""Day 20: Trench Map"""

def enhance(algorithm):
    return lambda window: algorithm[int(''.join(window), 2)]

def get_window(img, i, j, fill_value):
    window = []

    for x in (-1, 0, 1):
        if 0 <= i + x < len(img):
            row = ''

            for y in (-1, 0, 1):
                if 0 <= j + y < len(img[0]):
                    row += img[i+x][j+y]
                else:
                    row += fill_value

            window.append(row)
        else:
            window.append(str(fill_value) * 3)

    return window

def convolve(img, fill_value, fn):
    return [''.join(fn(get_window(img, i, j, fill_value))
             for j in range(-1, len(img) + 1))
            for i in range(-1, len(img[0]) + 1)]

def enhance_image(img, n):
    fill = '0'
    for _ in range(n):
        img = convolve(img, fill, enhance(algorithm))
        fill = algorithm[int(fill * 9, 2)]
    return img


if __name__ == '__main__':
    with open('input.txt') as f:
        algorithm = f.readline().strip().replace('#', '1').replace('.', '0')
        img = [l.replace('#', '1').replace('.', '0') for l in f.read().strip().splitlines()]

    print('part 1:', ''.join(enhance_image(img, 2)).count('1'))
    print('part 2:', ''.join(enhance_image(img, 50)).count('1'))
