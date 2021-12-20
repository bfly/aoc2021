from collections import defaultdict


def image_enhance_algorithm(_image, _pad):
    new_image = defaultdict(lambda: _pad)

    min_i = min(_image.keys(), key=lambda x: x[0])[0]
    min_j = min(_image.keys(), key=lambda x: x[1])[1]

    max_i = max(_image.keys(), key=lambda x: x[0])[0]
    max_j = max(_image.keys(), key=lambda x: x[1])[1]

    for _i in range(min_i - 1, max_i + 2):
        for _j in range(min_j - 1, max_j + 2):
            alg_index = [_image[(_i + x, _j + y)] for x, y in neighbours]
            alg_index_binary = int("".join([('1' if c == '#' else '0') for c in alg_index]), 2)
            new_image[(_i, _j)] = alg[alg_index_binary]

    return new_image


if __name__ == '__main__':
    fn = 'input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    with open(fn, 'r') as f:
        alg, inpt = f.read().split('\n\n')
        inpt = [list(row) for row in inpt.split('\n')]

    image = defaultdict(lambda: '.')

    for i, r in enumerate(inpt):
        for j, e in enumerate(r):
            image[(i, j)] = e

    neighbours = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    image_copy = image.copy()

    for part in [1, 2]:
        image = image_copy

        for s in range(2 if part == 1 else 50):
            pad = '.' if alg[0] == '.' else '#' if s % 2 == 0 else '.'

            image = image_enhance_algorithm(image, pad)

        count_lit = sum([1 for pixel in image.values() if pixel == '#'])
        print(f'Part {part}, {count_lit}')      # 5065, 14790
