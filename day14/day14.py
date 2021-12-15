from collections import Counter, defaultdict


def part1(pt, rules, steps):
    polymer = list(pt)
    print(f'Template:     {pt}')
    for step in range(1, steps + 1):
        i = 0
        while i < len(polymer) - 1:
            pair = ''.join(polymer[i:i + 2])
            if pair in rules:
                polymer.insert(i + 1, rules[pair])
            else:
                raise KeyError(f'Pair {pair} not in rules.')
            i += 2
        poly = ''.join(polymer)
        print(f'After step {step}: {poly}')
    poly = ''.join(polymer)
    counts = Counter(poly)
    print(f'Part 1: {max(counts.values()) - min(counts.values())}')
    print()


def part2(start, pairs, steps):
    occurence_map = defaultdict(int)
    for x in start:
        occurence_map[x] += 1
    pair_count = defaultdict(int)
    for pair in ("".join(pair) for pair in zip(start[:-1], start[1:])):
        pair_count[pair] += 1

    for _ in range(steps):
        for pair, count in pair_count.copy().items():
            new_char = pairs[pair]  # AC -> B
            occurence_map[new_char] += count  # add B
            pair_count[pair] -= count  # AC -> ABC, AC pair is gone
            pair_count[pair[0] + new_char] += count  # AB from ABC
            pair_count[new_char + pair[1]] += count  # BC from ABC

    print(f'Part 2: {max(occurence_map.values()) - min(occurence_map.values())}')


if __name__ == '__main__':
    template_rules = {}
    fn = 'input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    with open(fn, 'r') as f:
        lines = f.readlines()

        for line in lines:
            ln = line.rstrip('\n')
            if not ln:
                continue
            lin = ln.split()
            if len(lin) == 1:
                polymer_template = lin[0]
            elif len(lin) == 3 and lin[1] == '->':
                template_rules[lin[0]] = lin[2]

        print(f'{polymer_template=}, {template_rules=}')

        part1(polymer_template, template_rules, 10)

        part2(polymer_template, template_rules, 40)
