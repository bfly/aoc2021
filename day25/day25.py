import termcolor


def print_grid(_grid):
    for _row in _grid:
        print(''.join(_row))
    print()


def move_cucumber(_cucumber, _move_to):
    global seafloor
    _rf, _cf = cucumber
    _rt, _ct = move_to
    seafloor[_rf][_cf], seafloor[_rt][_ct] = seafloor[_rt][_ct], seafloor[_rf][_cf]  # exchange


if __name__ == '__main__':
    east = set()
    south = set()

    fn = 'input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    with open(fn, 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]

    seafloor = [[cell for cell in line] for line in lines]
    print(f'Initial state:')
    print_grid(seafloor)

    height = len(seafloor)
    width = len(seafloor[0])
    for i in range(height):
        row = seafloor[i]
        for j in range(width):
            if row[j] == '>':
                east.add((i, j))
            elif row[j] == 'v':
                south.add((i, j))

    moves = 1
    while True:
        new_east = set()
        has_moved = False
        for cucumber in east:
            move_to = (cucumber[0], (cucumber[1] + 1) % width)
            if move_to not in east and move_to not in south:
                has_moved = True
                new_east.add(move_to)
                move_cucumber(cucumber, move_to)
            else:
                new_east.add(cucumber)

        east = new_east

        new_south = set()
        for cucumber in south:
            move_to = ((cucumber[0] + 1) % height, cucumber[1])
            if move_to not in east and move_to not in south:
                has_moved = True
                new_south.add(move_to)
                move_cucumber(cucumber, move_to)
            else:
                new_south.add(cucumber)

        if not has_moved:
            break

        south = new_south

        moves += 1

        print(f'After {moves} steps:')
        print_grid(seafloor)

    print("Total moves", moves, '\n')
    MSG = 'MERRY CHRISTMAS!'
    for i, c in enumerate(MSG):
        color = 'red' if i % 2 == 0 else 'green'
        print(termcolor.colored(MSG[i:i + 1], color, 'on_grey', ['blink']), end='')
    print()
