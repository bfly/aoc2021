fn = 'input.txt'


if __name__ == '__main__':
    with open(fn, 'r') as f:
        nums = [line for line in f.readlines()]

    print(nums)