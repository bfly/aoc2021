from collections import defaultdict

fn = 'input.txt'
days = 256


if __name__ == '__main__':
    with open(fn, 'r') as f:
        nums_ = [int(num) for num in f.readline().rstrip().split(',')]

    print(f'Initially: {nums_} fish\n')

    nums = defaultdict(int)
    for num in nums_:
        nums[num] += 1

    for i in range(days):
        new_nums = defaultdict(int)
        for val, cnt in nums.items():
            print(f"{val=}, {cnt=}", end=' - ')
            if val == 0:
                new_nums[6] += cnt
                new_nums[8] += cnt
            else:
                new_nums[val - 1] += cnt

        print(f'#{i + 1}, {sum(new_nums.values()):,} fish')

        nums = new_nums
