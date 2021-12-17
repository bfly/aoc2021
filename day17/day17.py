def get_result(part):

    def trajectory(xv, yv, p):
        x, y, hmax = 0, 0, 0
        while x < max_x and y > min_y:
            x += xv     # The probe's x position increases by its x velocity.
            y += yv     # The probe's y position increases by its y velocity.
            if x in xrange and y in yrange:     # Within target area
                return hmax if p == 1 else True

            hmax = max(y, hmax)
            xv -= 1 if xv > 0 else 0  # The probe's x velocity decreases to zero, due to drag.
            yv -= 1     # The probe's y velocity decreases by 1, due to gravity.

        return False

    for dx in range(max_x + 1):
        for dy in range(min_y, 500):
            yield trajectory(dx, dy, part)


if __name__ == '__main__':
    fn = 'input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    with open(fn, 'r') as f:
        _, _, xr, yr = f.read().rstrip().split()
    print(f'Target range: {xr} {yr}')
    ix, iy = xr[2:].split('..'), yr[2:].split('..')
    x1, x2, y1, y2 = int(ix[0]), int(ix[1][:-1]), int(iy[0]), int(iy[1])
    xrange = range(min(x1, x2), max(x1, x2) + 1)
    yrange = range(min(y1, y2), max(y1, y2) + 1)
    max_x, min_y = max(xrange), min(yrange)

    print(f'Highest point that hits w/i the target area: {max(get_result(1))}')
    print(f'Initial velocities that hit w/i target area: {sum(get_result(2))}')
