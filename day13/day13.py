from collections import namedtuple

import numpy as np

Mark = '#'


def pprint(list2d):
    # print(f'Printing {len(list2d)} rows, {len(list2d[0])} columns.')
    for row in list2d:
        for cell in row:
            print(cell, end='')
        print()


def fold_list(coord, num):
    larger, smaller = [], []
    axis = 0
    if coord == "x":
        axis = 1
        larger = [r[:num] for r in grid]
        smaller = [r[num+1:] for r in grid]
    elif coord == "y":
        axis = 0
        larger = grid[:num]
        smaller = grid[num+1:]
    smaller = np.flip(smaller, axis)
    new_grid = list(larger)
    for i in range(len(smaller)):
        for j in range(len(smaller[i])):
            if smaller[i][j] == "#":
                x_offset = len(larger)-len(smaller)
                y_offset = len(larger[0])-len(smaller[0])
                new_grid[i+x_offset][j+y_offset] = "#"
    return new_grid


if __name__ == '__main__':
    points = []
    folding = []
    Point = namedtuple('Point', 'x y')
    fn = 'input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    with open(fn, 'r') as f:
        lines = f.readlines()

        for line in lines:
            # print(f'{line=}')
            if not line.rstrip('\n'):
                continue
            if line[:4] == 'fold':
                folding.append(line.rstrip('\n'))
                continue
            no, y = line.rstrip('\n').split(',')
            if no.isdigit() and y.isdigit():
                points.append(Point(int(no), int(y)))
    print(f'{points=}')
    maxX, maxY = 0, 0
    for point in points:
        maxX = max(maxX, point.x)
        maxY = max(maxY, point.y)
    print(f'{maxX=}, {maxY=}\n')

    grid = [['.' for _ in range(maxX + 1)] for _ in range(maxY + 1)]
    for point in points:
        grid[point.y][point.x] = Mark
    # pprint(grid, len(grid))

    for fold in folding:
        dir, no = fold.split(' ')[2].split('=')
        print(f"Fold along {dir} = {no}.")

        grid = fold_list(dir, int(no))

        res = sum(row.count("#") for row in grid)

        pprint(grid)
        print(f'{res} marks')
        print()
