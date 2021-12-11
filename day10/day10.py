fn = 'short.txt'

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
starts = ['(', '[', '{', '<']
ends = [')', ']', '}', '>']
points2 = {')': 1, ']': 2, '}': 3, '>': 4}
pairs = {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
    '<': '>',
    '>': '<',
}

chunk = {}


def check_chunk(chunk):
    if all(chunk.values() == 0):
        return 'good'
    return False


def part1(lines):
    illegal_chars = []
    corrupted_lines = []
    for i, line in enumerate(lines):
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
                corrupted_lines.append(i)
                break

    print(f'Total illegal points: {sum([points[char] for char in illegal_chars])}')

    corrupted_lines.sort(reverse=True)
    for i in corrupted_lines:       # Remove corrupted lines
        del lines[i]


def return_missing(line):
    stack = []
    for c in line:
        if c in starts:
            stack.append(c)
        else:
            if stack[-1] == pairs[c]:
                stack.pop()
    return [pairs[s] for s in stack]


def part2(lines):
    scores = []
    for line in lines:
        missing = return_missing(line.strip('\n'))
        missing.reverse()
        score = 0
        for m in missing:
            score = score * 5 + points2[m]
        print(f'{score=:,},\t{missing=}')
        scores.append(score)

    scores.sort()
    print(f'{scores=}')
    print(scores[len(scores) // 2])


if __name__ == '__main__':
    fn = 'input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    with open(fn, 'r') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)
