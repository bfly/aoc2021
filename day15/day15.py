
import networkx as nx


def pprint(list2d):
    for row in list2d:
        for cell in row:
            print(cell, end='')
        print()


def part1(arr):
    width, height = len(arr), len(arr[0])

    graph = nx.DiGraph()
    for x, y in [(x, y) for x in range(width) for y in range(height)]:
        for new_x, new_y in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            try:
                graph.add_edge((x, y), (new_x, new_y), weight=arr[new_x][new_y])
            except IndexError:
                pass

    total_risk = nx.shortest_path_length(graph, (0, 0), (width - 1, height - 1), weight="weight")
    # path = nx.shortest_path(graph, (0, 0), (width - 1, height - 1), weight="weight")
    print(f'Part 1 risk: {total_risk}')


def part2(arr):
    width, height = len(arr), len(arr[0])
    l_width, l_height = width * 5, height * 5

    graph = nx.DiGraph()
    for x, y in [(x, y) for x in range(l_width) for y in range(l_height)]:
        cost = arr[x % width][y % height] + x // width + y // height
        if cost > 9:
            cost %= 9
        for new_x, new_y in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            graph.add_edge((new_x, new_y), (x, y), weight=cost)

    total_risk = nx.shortest_path_length(graph, (0, 0), (l_width - 1, l_height - 1), weight="weight")
    print(f'Part 2 risk: {total_risk}')


if __name__ == '__main__':
    fn = 'input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    with open(fn, 'r') as f:
        num_list = [list(map(int, list(line.strip('\n')))) for line in f.readlines()]
        # pprint(num_list)

        part1(num_list)
        part2(num_list)
