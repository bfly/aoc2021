import itertools
from functools import cache
from itertools import cycle


def part1(_course: [int], point_limit):
    points = [0, 0]
    rolls = 0
    die = cycle(range(1, 101)).__next__

    while True:
        for _i in range(2):
            rolls += 3
            p = [die() for _ in range(3)]
            _course[_i] += sum(p)
            while _course[_i] > 10:
                _course[_i] -= 10
            points[_i] += course[_i]
            # print(f'Player {_i + 1} rolls {p[0]}+{p[1]}+{p[2]} and moves to space {_course[_i]}
            # for a total score of {points[_i]}.')
            if points[_i] >= point_limit:
                return min(points[0], points[1]) * rolls


def part2(a_pos, b_pos, score_limit):
    return max(quantum_game(a_pos, 0, b_pos, 0, True, score_limit))


@cache
def quantum_game(a_pos, a_score, b_pos, b_score, a_turn, score_limit):
    if a_score >= score_limit:
        return 1, 0
    if b_score >= score_limit:
        return 0, 1
    pos = a_pos if a_turn else b_pos
    new_positions = [(pos + throw - 1) % 10 + 1 for throw in throws]
    if a_turn:
        subgames = (quantum_game(new_p, a_score + new_p, b_pos, b_score, False, score_limit)
                    for new_p in new_positions)
    else:
        subgames = (quantum_game(a_pos, a_score, new_p, b_score + new_p, True, score_limit)
                    for new_p in new_positions)
    return sum(a for a, _ in subgames), sum(b for _, b in subgames)


if __name__ == '__main__':
    throws = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]
    DEBUG = len(input('s(ubmit) else ENTER ')) == 0
    fn = 'short.txt' if DEBUG else 'input.txt'
    with open(fn, 'r') as f:
        course = [int(f.readline().split()[-1]) for _ in range(2)]

        course_save = course.copy()

        ans = part1(course, 1000)
        if DEBUG:
            assert ans == 739785

        print(f'Part 1: {ans:,}')       # 739,785 - 989,352

        course = course_save.copy()

        ans = part2(course[0], course[1], 21)
        if DEBUG:
            assert ans == 444356092776315

        print(f'Part 2: {ans:,}')
