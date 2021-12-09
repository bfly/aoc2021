fn = 'input.txt'
# https://github.com/DecemberDream/advent-of-code


def part1(lines):
    res1 = 0
    for line in lines:
        _, right = line.split('|')
        y = right.split(' ')

        for num in y:
            if len(num) in {2, 3, 4, 7}:
                res1 += 1
    print(f'{res1=}')


def part2(lines):
    left = []
    right = []

    for line in lines:
        split_line = line.split("|")
        left.append(["".join(sorted(c)) for c in split_line[0].split()])
        right.append(["".join(sorted(c)) for c in split_line[1].split()])

    res2 = 0

    for i in range(len(left)):
        digits = {}

        while len(digits) < 10:
            for digit in left[i]:
                # trivial cases
                if len(digit) == 2 and 1 not in digits:
                    digits[1] = digit
                    continue
                if len(digit) == 3 and 7 not in digits:
                    digits[7] = digit
                    continue
                if len(digit) == 4 and 4 not in digits:
                    digits[4] = digit
                    continue
                if len(digit) == 7 and 8 not in digits:
                    digits[8] = digit
                    continue

                # either 2 or 5 or 3
                if len(digit) == 5:
                    if 7 in digits and all([i in list(digit) for i in list(digits.get(7))]):
                        digits[3] = digit
                    elif 9 in digits and all([i in list(digits.get(9)) for i in list(digit)]):
                        digits[5] = digit
                    elif 9 in digits:
                        digits[2] = digit

                # either 0 or 6 or 9
                if len(digit) == 6:
                    if 3 in digits and all([i in list(digit) for i in list(digits.get(3))]):
                        digits[9] = digit
                    elif 5 in digits and sum([i in list(digits.get(5)) for i in list(digit)]) == 5:
                        digits[6] = digit
                    elif 5 in digits and sum([i in list(digits.get(5)) for i in list(digit)]) == 4:
                        digits[0] = digit

        out_num_1 = []

        for out_pos in range(4):
            out_num_1.append([k for k, v in digits.items() if v == right[i][out_pos]][0])

        res2 += int("".join([str(c) for c in out_num_1]))
    print(f'{res2=}')


if __name__ == '__main__':
    with open(fn, 'r') as f:
        data = f.read().splitlines()
        part1(data)
        part2(data)
