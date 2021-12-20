# let x,xi be the x-coordinates of scanner 0 and i.
# pts[i] is list of all points for scanner i.
# foundPts is a set of all distinct points in ref of (0,0,0) in direction (1,1,1)
# first loop through foundPts and pts[i] and take 2 pairs of points as the same for now
# then for all permutation and [+-1,+-1,+-1] directions we can calculate (x1,y1,z1)
# with that as ref now we should deref points into (0,0,0) pov and check if there is 11 more points matching
# if yes then we can take the coords of xi as perm(x1,y1,z1)*(directionVector(+-1,+-1,+-1))
# add all these points to foundPts and continue the same with remaining points


from itertools import permutations


# returns the point after resolving permutation and direction vectors
def get_point(_pt, perm, _dir):
    newpt = _pt.copy()
    for _i in range(3):
        newpt[_i] = _pt[perm[_i] - 1] * _dir[_i]
    return newpt


def subtract_point(pt1, pt2):
    newpt = pt1.copy()
    for _i in range(3):
        newpt[_i] -= pt2[_i]
    return newpt


def add_point(pt1, pt2):
    newpt = pt1.copy()
    for _i in range(3):
        newpt[_i] += pt2[_i]
    return newpt


def compute(indx0, indx1, _inp, fnd, bfnd, fnd_pts):
    permlist = list(permutations(range(1, 4)))
    for pt1 in _inp[indx0]:
        for pt2 in _inp[indx1]:
            for perm in permlist:
                for di in range(-1, 2, 2):
                    for dj in range(-1, 2, 2):
                        for dk in range(-1, 2, 2):
                            newpt2 = get_point(pt2, perm, [di, dj, dk])
                            scanner2 = subtract_point(pt1, newpt2)
                            matching = 1
                            unmatchingPts = []
                            newinp = []
                            for pt3 in _inp[indx1]:
                                newpt3 = get_point(pt3, perm, [di, dj, dk])
                                realPt3 = add_point(newpt3, scanner2)
                                newinp.append(realPt3)
                                if pt3 == pt2:
                                    continue
                                if _inp[indx0].__contains__(realPt3):
                                    matching += 1
                                else:
                                    unmatchingPts.append(realPt3)
                            if matching >= 12:
                                _inp[indx1] = newinp
                                for pts in unmatchingPts:
                                    fnd_pts.add(tuple(pts))
                                fnd[indx1] = scanner2
                                bfnd[indx1] = True
                                return


# part 2
def get_manhattan_distance(pt1, pt2):
    res = 0
    for _i in range(3):
        res += abs(pt1[_i] - pt2[_i])
    return res


def part2():
    maxManhattanDistance = 0
    for _i in range(n):
        for j in range(n):
            maxManhattanDistance = max(maxManhattanDistance, get_manhattan_distance(found[_i], found[j]))
    return maxManhattanDistance


if __name__ == '__main__':
    fn = 'input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    inp, temp = [], []
    with open(fn, 'r') as f:
        lines = [str(line.strip()) for line in f.readlines()]
        for line in lines:
            if len(line) == 0:
                inp.append(temp)
                temp = []
                continue
            if not line.__contains__("scanner"):
                temp.append(list(map(int, line.split(','))))
        inp.append(temp)
        temp = []
        n = len(inp)
        print(n)
        found = [[] for _ in range(n)]      # [x,y,z]
        bfound = [False for _ in range(n)]
        found[0] = [0, 0, 0]
        bfound[0] = True
        foundPts = set()
        for pt in inp[0]:
            foundPts.add(tuple(pt))
        q = [0]
        while len(q) > 0:
            print(q)
            indx = q.pop()
            for i in range(n):
                if i == indx:
                    continue
                if not bfound[i]:
                    compute(indx, i, inp, found, bfound, foundPts)
                    if bfound[i]:
                        q.append(i)

    print(len(foundPts))    # 359

    print(part2())          # 12292
