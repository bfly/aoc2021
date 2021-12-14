from collections import defaultdict


def dfs(graph, source, target, path, paths, revisits):
    if source in path and source.islower():
        revisits = False

    path.append(source)

    if source == target:
        paths.append(path.copy())

    else:
        for node in graph[source]:

            if revisits:
                valid_node = not (node == 'start')
            else:
                valid_node = not (node in path and node.islower())

            if valid_node:
                dfs(graph, node, target, path, paths, revisits)

    path.pop()      # backtrack if target reached or no neighbours are valid

    return paths


if __name__ == '__main__':
    graph_dict = defaultdict(lambda: [])
    names = {'1': 'short.txt', '2': 'medium.txt', '3': 'longer.txt', '4': 'input.txt'}
    print(names, end=': ')
    x = input()
    fn = names[x] if x in names else 'short.txt'

    with open(fn) as f:
        lines = f.readlines()
        for line in lines:
            f, t = line.rstrip('\n').split('-')
            graph_dict[f].append(t)
            graph_dict[t].append(f)

        print('\nPart 1:')
        all_paths = dfs(graph_dict, 'start', 'end', [], [], revisits=False)
        print(f'{all_paths=}, {len(all_paths)}')

        print('\nPart 2:')
        all_paths = dfs(graph_dict, 'start', 'end', [], [], revisits=True)
        print(f'{all_paths=}, {len(all_paths)}')
