
def part1(lines):
    pass


def part2(lines):
    pass


if __name__ == '__main__':
    fn = 'input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    with open(fn, 'r') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)
