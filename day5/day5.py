from collections import namedtuple

fn = 'input.txt'


def print_grid(grid, size):
    if fn == 'short.txt':
        for col in range(0, size):
            for row in range(0, size):
                point = Point(row, col)
                if point in grid:
                    print(grid[point], end='')
                else:
                    print('.', end='')
            print()
        print()
    count = 0
    for g in grid.keys():
        if grid[g] > 1:
            if fn == 'short.txt':
                print(g, grid[g])
            count += 1
    print(f'Overlaps = {count}')


def incr_grid(point, grid):
    if point in grid:
        grid[point] += 1
    else:
        grid[point] = 1


def load_points():
    f_points = []
    t_points = []
    max_x = max_y = 0
    file = open(fn, 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        tokens = line.split()
        fx = tokens[0].split(',')
        tx = tokens[2].split(',')
        from_point = Point(int(fx[0]), int(fx[1]))
        thru_point = Point(int(tx[0]), int(tx[1]))
        max_x = max(max_x, max(from_point.x, thru_point.x))
        max_y = max(max_y, max(from_point.y, thru_point.y))
        f_points.append(from_point)
        t_points.append(thru_point)
    return f_points, t_points, len(lines)


def load_grid(diagonal):
    grid = {}
    for p in range(len(from_points)):
        x1, y1 = from_points[p]
        x2, y2 = thru_points[p]
        stepx = 1 if x2 > x1 else -1
        stepy = 1 if y2 > y1 else -1
        stepx = 0 if x1 == x2 else stepx
        stepy = 0 if y1 == y2 else stepy
        if diagonal:
            while True:
                incr_grid(Point(x1, y1), grid)
                x1 += stepx
                y1 += stepy
                if x1 == x2 and y1 == y2:
                    break
            incr_grid(Point(x1, y1), grid)
        else:
            if x1 == x2:
                for y in range(y1, y2 + stepy, stepy):
                    incr_grid(Point(x1, y), grid)
            if y1 == y2:
                for x in range(x1, x2 + stepx, stepx):
                    incr_grid(Point(x, y1), grid)
    print_grid(grid, grid_size)


if __name__ == '__main__':
    Point = namedtuple('Point', 'x, y')
    from_points, thru_points, grid_size = load_points()

    load_grid(diagonal=False)
    print('\n' + 25*'-' + '\n')
    load_grid(diagonal=True)
