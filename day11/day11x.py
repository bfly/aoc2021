from itertools import product

with open("input.txt", 'r') as f:
    grid = [list(map(int, list(line.rstrip()))) for line in f.readlines()]

steps = 100


def flash(i, j, flashed):
    flashed[i][j] = True

    def neighbours(cell):
        for c in product(*(range(n - 1, n + 2) for n in cell)):
            if c != cell and all(0 <= n < len(grid) for n in c):
                yield c

    for x, y in neighbours((i, j)):
        grid[x][y] += 1

    return flashed


flashes_cnt = 0
s = 1
while True:
    flashed = [[False for i in range(len(grid))] for j in range(len(grid[0]))]
    stack = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = grid[i][j] + 1

            if grid[i][j] > 9:
                stack.add((i, j))

    while stack != set():

        x, y = stack.pop()

        flashed = flash(x, y, flashed)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9 and flashed[i][j] is False:
                    stack.add((i, j))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if flashed[i][j]:
                grid[i][j] = 0

    flashes_cnt += sum([x for r in flashed for x in r])

    if sum([x for r in flashed for x in r]) == len(grid) * len(grid[0]):
        print("step: " + str(s))
        break

    s += 1

print(flashes_cnt)
