from functools import reduce

fn = 'input.txt'

adjs = [[-1, 0], [0, +1], [+1, 0], [0, -1]]  # Adjacent cell positions


def valid_cell(n, r, c):
    return 0 <= r < len(n) and 0 <= c < len(n[r])  # Row and colmnn coordinates within grid


def num_is_low(n, r, c):  # Is this point less than their adjacent cells
    this = n[r][c]
    lows, valids = 0, 0
    for i, j in get_adjacent_cells(n, r, c):  # For each adjacent cell
        valids += 1  # Count adjacent cell
        if this < n[i][j]:  # Low point
            lows += 1
    return lows == valids  # This point lower than all the adjacent cells


def part1(nums):
    low_point_vals, low_points = [], []
    for r, row in enumerate(nums):  # For each row in heightmap
        for col, num in enumerate(row):  # For column value in heightmap
            if num_is_low(nums, r, col):  # Check if the point is a low point
                low_point_vals.append(num)  # Capture low point value
                low_points.append((r, col))  # Capture low point coordinates
    risks = [low + 1 for low in low_point_vals]  # Risk value is low point value + 1
    print(f'Pass 1 total risk level is {sum(risks)}.')
    return low_points  # List of low points for point 2


def get_adjacent_cells(n, r, c):
    neighbors = set()
    for rx, cx in adjs:  # For each adjacent cell
        if valid_cell(n, r + rx, c + cx):  # Valid cell
            neighbors.add((r + rx, c + cx))  # Add to the neighbors list
    return neighbors


def part2(nums, lows):
    basin_sizes = []
    for x, y in lows:  # For each low point
        visited = [(x, y)]  # To not duplicate basin points
        queue = [(x, y)]  # Queue to find all basins arounf low points
        size = 1  # Count thw low point
        while queue:
            x, y = queue.pop()
            for i, j in get_adjacent_cells(nums, x, y):  # Get adjacent cells for each point
                if nums[i][j] != 9 and (i, j) not in visited:  # Still wiyjin basin and not a duplicate point
                    visited.append((i, j))  # Add point to visited list
                    queue.append((i, j))  # Add point to queue to check its neighbors
                    size += 1  # Add 1 to basin size
        basin_sizes.append(size)

    basin_sizes.sort(reverse=True)  # Sort basin sizes in descending order
    # Find the product of the top 3 basin sizes using a reduce function, lambda, and list slicing
    print(f'Pass 2 total basin sizes is {reduce(lambda a, b: a * b, basin_sizes[:3])}.')


if __name__ == '__main__':
    with open(fn) as f:
        num_list = [list(map(int, list(line.strip('\n')))) for line in f.readlines()]

    lows_points = part1(num_list)  # Find the low points in heightmap
    part2(num_list, lows_points)  # Find the product of top 3 basin sizes

"""
Pass 1 total risk level is 539.
Pass 2 total basin sizes is 736920.
"""
