
with open("input.txt", 'r') as f:
    nums = [line.rstrip() for line in f.readlines()]

outs = []

for i in range(len(nums[0])):
    out = []
    one = zero = 0
    for num in nums:
        if num[i] == '1':
            one += 1
        else:
            zero += 1

    if one > zero:
        out.append('1')
    else:
        out.append('0')

    outs.append("".join(out))

gamma = int("".join(outs), 2)
epsilon = pow(2, len(nums[0])) - gamma - 1

print(f'{gamma=}, {epsilon=}, {gamma * epsilon=}')

nums_o = num_c = nums


def getCommon(nums, i):
    zero = one = 0
    for num in nums:
        if num[i] == '0':
            zero += 1
        else:
            one += 1
    return zero, one


i = 0
while len(nums_o) > 1:
    zero, one = getCommon(nums_o, i)
    choice = '1' if one >= zero else '0'
    nums_o = list(filter(lambda x: x[i] == choice, nums_o))
    i += 1

o2 = int("".join(nums_o), 2)

i = 0
while len(num_c) > 1:
    zero, one = getCommon(num_c, i)
    choice = '0' if one >= zero else '1'
    num_c = list(filter(lambda x: x[i] == choice, num_c))
    i += 1

co2 = int("".join(num_c), 2)

print(f'{o2=}, {co2=}, {o2 * co2=}')
