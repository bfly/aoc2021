grid = []
flashed = []
stack = []
flashes = 0


def pprint(list2d):
    width = len(list2d)
    for row in list2d:
        for c, cell in enumerate(row):
            print(cell, end='')
        print()
    print()


def flash(i, j):
    global flashed, grid, stack, flashes

    flashed[i][j] = True
    grid[i][j] = 0
    stack.append((i, j))
    flashes += 1
    # print(f'{i=}, {j=}, flashed')


def init_flashed():
    global flashed, grid
    flashed = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]


def process_step():
    global stack
    stack = []
    init_flashed()
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            grid[r][c] += 1
            if grid[r][c] > 9:
                flash(r, c)  # flash
    while stack:
        r, c = stack.pop()
        increment_neighbors(r, c)


def increment_neighbors(r, c):
    global flashed, grid

    for rx, cx in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        i = r + rx
        j = c + cx
        if 0 <= i < len(grid) and 0 <= j < len(grid):
            if not flashed[i][j]:
                grid[i][j] += 1
                if grid[i][j] > 9:
                    flash(i, j)     # flash


def part1(part, steps):
    global flashed, grid, stack

    for step in range(steps):
        process_step()

        if part == 1:
            if step < 10 or (step + 1) % 10 == 0:
                print(f'\nAfter step {step + 1}:')
                pprint(grid)
            if step + 1 == 10 or step + 1 == 100:
                print(f'{flashes} flashes')
        else:
            if step >= 192:
                print(f'\nAfter step {step + 1}:')
                pprint(grid)
                sumit = 0
                for subl in grid:
                    for item in subl:
                        sumit += item
                if sumit == 0:
                    return


def part2():
    global flashed, grid, stack

    print('\nPart 2:')
    step = 0
    sumit = -1
    while sumit != 0:
        process_step()
        step += 1
        if step >= 193:
            pprint(grid)
        print(step, end=', ')
        sumit = 0
        for subl in grid:
            for item in subl:
                sumit += item

    print()
    pprint(grid)
    print(f'{step=}')


if __name__ == '__main__':
    save = []
    fn = 'input.txt' if input('s(ubmit) else ENTER ').lower() == 's' else '10x10.txt'
    with open(fn, 'r') as f:
        steps = int(f.readline())
        lines = f.readlines()
        for line in lines:
            row = [int(x) for x in line.rstrip('\n')]
            grid.append(row)
            save.append(row)
        print('Before any steps:')
        pprint(grid)

        part1(1, steps)

        grid = save
        print('Before any steps:')
        pprint(save)
        part1(2, 9999)
