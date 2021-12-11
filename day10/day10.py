fn = 'short.txt'

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
starts = ['(', '[', '{', '<']
ends = [')', ']', '}', '>']
idx = {')': 0, ']': 1, '}': 2, '>': 3}

chunk = {}


def check_chunk(chunk):
    if all(chunk.values() == 0):
        return 'good'
    return False


def part1(lines):
    illegal_chars = []
    for line in lines:
        stack = []
        for char in line.strip('\n'):
            is_ci = char == ends[0] and len(stack) > 0 and stack[-1] == starts[0]
            is_sq = char == ends[1] and len(stack) > 0 and stack[-1] == starts[1]
            is_cl = char == ends[2] and len(stack) > 0 and stack[-1] == starts[2]
            is_gt = char == ends[3] and len(stack) > 0 and stack[-1] == starts[3]
            if is_gt or is_sq or is_cl or is_ci:
                stack.pop()
            elif char in starts:
                stack.append(char)
            else:
                # Collect all illegal chars
                illegal_chars.append(char)
                break


    print(f'Total illegal points: {sum([points[char] for char in illegal_chars])}')


if __name__ == '__main__':
    with open(fn, 'r') as f:
        lines = f.readlines()
        part1(lines)
