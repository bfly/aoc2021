grid = []
flashed = []


def pprint(list2d, width):
    for row in list2d:
        for c, cell in enumerate(row):
            if c == width - 1:
                print(cell)
            else:
                print(cell, end=', ')


def increment_neighbors(r, c):
    global flashed, grid
    print(f'\tincrement neighbors: {r=}, {c=}')
    for rx, cx in [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]:
        i = r + rx
        j = c + cx
        if not flashed[i][j]:
            grid[i][j] += 1
            if grid[i][j] > 9:
                grid[i][j] = 0  # flashes
                print(f'\t\tFlash: {i=}, {j=}, {grid[i][j]=}')
                flashed[i][j] = True
                increment_neighbors(i, j)


def part1(steps):
    global flashed, grid

    for step in range(steps):
        print(f'\nStep {step + 1}')
        flash, flash_row = [], []
        for _ in range(len(grid)):
            flash_row.append(False)
        for _ in range(len(grid)):
            flashed.append(flash_row)
        print('flashed initialized to False')
        pprint(flashed, width=len(flashed))

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                grid[r][c] += 1
                if grid[r][c] > 9:
                    grid[r][c] = 0  # flashed
                    print(f'\tFlash: {r=}, {c}, {grid[r][c]=}')
                    flashed[r][c] = True
                    increment_neighbors(r, c)
        print(f'\nAfter step {step + 1}:')
        pprint(grid, width=len(grid))


def part2(grid):
    pass


if __name__ == '__main__':
    fn = 'input.txt' if input('s(ubmit) else ENTER ') else '5x5.txt'
    with open(fn, 'r') as f:
        steps = int(f.readline())
        lines = f.readlines()
        for line in lines:
            row = [int(x) for x in line.rstrip('\n')]
            grid.append(row)
        print('Before any steps:')
        pprint(grid, width=5)
        save = grid.copy()

        part1(steps)
        part2(save)
