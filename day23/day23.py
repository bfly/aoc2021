
import sys
from collections import Counter
from copy import deepcopy

from niceprint import MultiColoredPrint as mcp
from pytictoc import TicToc

# Part 1 - short.txt = 12521
# A = ['B', 'A']
# B = ['C', 'D']
# C = ['B', 'C']
# D = ['D', 'A']
# expected = 12521

# Part 1 - input.txt = 19019
# A = ['D', 'D']
# B = ['B', 'A']
# C = ['C', 'B']
# D = ['C', 'A']
# expected = 19019

# Part 2 = short.txt = 44169
# A = ['B', 'D', 'D', 'A']
# B = ['C', 'C', 'B', 'D']
# C = ['B', 'B', 'A', 'C']
# D = ['D', 'A', 'C', 'A']
# expected = 44169

# Part 2 - input.txt = 47533
A = ['D', 'D', 'D', 'D']
B = ['B', 'C', 'B', 'A']
C = ['C', 'B', 'A', 'B']
D = ['C', 'A', 'C', 'A']
expected = 47533

hallway = ['E' for _ in range(11)]

start = ({'A': A, 'B': B, 'C': C, 'D': D}, hallway)
final_state = ()

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

DP = {}


def done(_state):
    bot, top = _state
    for k, v in bot.items():
        for vv in v:
            if vv != k:
                return False
    return True


def can_move_from(k, col):
    for c in col:
        if c != k and c != 'E':
            return True
    return False


def can_move_to(k, col):
    for c in col:
        if c != k and c != 'E':
            return False
    return True


def bot_idx(bot):
    return {'A': 2, 'B': 4, 'C': 6, 'D': 8}[bot]


def top_idx(col):
    for i, c in enumerate(col):
        if c != 'E':
            return i
    return None


def dest_idx(col):
    for i, c in reversed(list(enumerate(col))):
        if c == 'E':
            return i
    return None


def between(a, bot, top):
    # 0 1 A 3 B 5 C 7 D 9 10
    return (bot_idx(bot) < a < top) or (top < a < bot_idx(bot))


assert between(1, 'A', 0)


def clear_path(bot, _top_idx, top):
    for ti in range(len(top)):
        if between(ti, bot, _top_idx) and top[ti] != 'E':
            return False
    return True


def show(_state):
    bot, top = _state
    _C = Counter()
    for c in top:
        _C[c] += 1
    for k, v in bot.items():
        for c in v:
            _C[c] += 1


def print_burrow(_state):
    bot, top = _state
    print(13 * '#')
    _hallway = ''.join(top).replace('E', '.')
    print('#' + _hallway + '#')
    _A, _B, _C, _D = bot.values()
    for _r in range(len(_A)):
        line = '###' if _r == 0 else '  #'
        line += _A[_r] + '#' + _B[_r] + '#' + _C[_r] + '#' + _D[_r] + '#'
        if _r == 0:
            line += '##'
        line.replace('E', '.')
        print(line)
    print('  ' + 9 * '#')
    print()


def main(_state):
    global final_state
    # given a state, what is the cost to get to "done"?
    show(_state)
    # move top -> L or R
    # move L or R ->
    # always move to destination ASAP
    bottom, top = _state
    key = (tuple((k, tuple(v)) for k, v in bottom.items()), tuple(top))
    if done(_state):
        final_state = _state
        return 0
    if key in DP:
        return DP[key]
    # move to destination, if possible
    for i, c in enumerate(top):
        if c in bottom and can_move_to(c, bottom[c]):
            if clear_path(c, i, top):
                di = dest_idx(bottom[c])
                assert di is not None
                distance_moved = di + 1 + abs(bot_idx(c) - i)
                cost = COST[c] * distance_moved
                new_top = list(top)
                new_top[i] = 'E'
                top[i] = 'E'
                new_bottom = deepcopy(bottom)
                new_bottom[c][di] = c
                return cost + main((new_bottom, new_top))

    answer = sys.maxsize
    for k, col in bottom.items():
        if not can_move_from(k, col):
            continue
        ki = top_idx(col)
        if ki is None:
            continue
        c = col[ki]
        for to_ in range(len(top)):
            if to_ in [2, 4, 6, 8]:
                continue
            if top[to_] != 'E':
                continue
            if clear_path(k, to_, top):
                distance_moved = ki + 1 + abs(to_ - bot_idx(k))
                new_top = list(top)
                assert new_top[to_] == 'E'
                new_top[to_] = c
                new_bottom = deepcopy(bottom)
                assert new_bottom[k][ki] == c
                new_bottom[k][ki] = 'E'
                answer = min(answer, COST[c] * distance_moved + main((new_bottom, new_top)))

    DP[key] = answer
    return answer


if __name__ == '__main__':
    t = TicToc()
    t.tic()
    print_burrow(start)
    actual = main(start)
    print_burrow(final_state)
    if actual != expected:
        print(f'Expected {expected} not equal Actual {actual}.')
    print('Least energy required to organize the amphipods is', end=' ')
    mcp(actual, color="r")
    t.toc()
