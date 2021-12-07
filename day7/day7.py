import math

from pytictoc import TicToc

fn = 'input.txt'


def calc_min_fuel_cost():
    t = TicToc()
    t.tic()
    min_pos, max_pos = min(nums), max(nums)
    fuel_cost_con, fuel_cost_esc = max_pos * len(nums), math.factorial(max_pos * len(nums))
    level_con, level_esc = min_pos, min_pos
    for pos in range(min_pos, max_pos + 1):
        fuel_con, fuel_esc = 0, 0
        for num in nums:
            dist = abs(num - pos)
            fuel_con += dist
            fuel_esc += int(dist * (dist + 1) / 2)
        if fuel_con < fuel_cost_con:
            fuel_cost_con, level_con = fuel_con, pos
        if fuel_esc < fuel_cost_esc:
            fuel_cost_esc, level_esc = fuel_esc, pos

    print(f'{level_con=}, {fuel_cost_con=}')
    print(f'{level_esc=}, {fuel_cost_esc=}')
    t.toc()


if __name__ == '__main__':
    with open(fn, 'r') as f:
        nums = [int(num) for num in f.readline().rstrip().split(',')]

    print(nums)

    calc_min_fuel_cost()
    # constant_fuel_cost, level=339, fuel_cost=328318
    # escalating_fuel_cost, level=467, fuel_cost=89791146
