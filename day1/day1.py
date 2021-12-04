with open("input.txt") as file:
    nums = [int(line) for line in file.readlines()]


nums = [sum(nums[i-2:i+1]) for i in range(2, len(nums))]  # part 2

count = 0


for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1

# print(count)

# one line
part1 = len([i for i in range(1, len(nums)) if nums[i] > nums[i-1]])
part2 = len([i for i in range(3, len(nums)) if sum(nums[i-2:i+1]) > sum(nums[i-3:i])])
print(f'{part1=}')
print(f'{part2=}')
