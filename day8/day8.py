
def format_vals(input_val):
    return list(map(lambda w: ''.join(sorted(w)), input_val))


def part1(inputs):
    ans = sum(
        len(chars) in (2, 3, 4, 7)
        for line in inputs
        for chars in line.split('|')[1].strip().split()
    )
    print(f'Part 1: The digits 1, 4, 7, or 8 appear {ans}')


def part2(inputs):
    outputs = list(map(format_vals, [input_val.split('|')[1].strip().split() for input_val in inputs]))
    inputs = list(map(format_vals, [input_val.split('|')[0].strip().split() for input_val in inputs]))

    code = []
    mapping = {2: 1, 3: 7, 4: 4, 7: 8}
    for input_val in inputs:
        temp = {}
        for word in input_val:
            if len(word) in mapping:
                temp[mapping[len(word)]] = word

        # Find 6
        for word in input_val:
            if len(word) == 6 and any(char not in word for char in temp[1]):
                temp[6] = word
                break
        # Find 0
        for word in input_val:
            if len(word) == 6 and any(char not in word for char in temp[4]) and word not in temp.values():
                temp[0] = word
                break

        # Find 9 after 6 and 0 with length 6
        for word in input_val:
            if len(word) == 6 and word not in temp.values():
                temp[9] = word
                break
        # Find 5
        for word in input_val:
            if len(word) == 5 and all(char in temp[6] for char in word):
                temp[5] = word
                break

        # Find 3
        for word in input_val:
            if len(word) == 5 and all(char in temp[9] for char in word) and word not in temp.values():
                temp[3] = word
                break

        # Find 2 after 3 and 5 with length 5
        for word in input_val:
            if len(word) == 5 and word not in temp.values():
                temp[2] = word

        # Transform key-value to value-key
        code.append({v: k for k, v in temp.items()})
    total = 0
    for i, output in enumerate(outputs):
        total += int(''.join(map(str, [code[i][word] for word in output])))
    print(f'Part 2: Sum of the output values is {total}')


if __name__ == '__main__':
    input_vals = open('input.txt').readlines()
    part1(input_vals)
    part2(input_vals)
