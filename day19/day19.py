def rotations(scanner):
    rots = []
    for i in range(24):
        rots.append([])
    for coord in scanner:
        # positive x
        rots[0].append((+coord[0], +coord[1], +coord[2]))
        rots[1].append((+coord[0], -coord[2], +coord[1]))
        rots[2].append((+coord[0], -coord[1], -coord[2]))
        rots[3].append((+coord[0], +coord[2], -coord[1]))
        # negative x
        rots[4].append((-coord[0], -coord[1], +coord[2]))
        rots[5].append((-coord[0], +coord[2], +coord[1]))
        rots[6].append((-coord[0], +coord[1], -coord[2]))
        rots[7].append((-coord[0], -coord[2], -coord[1]))
        # positive y
        rots[8].append((+coord[1], +coord[2], +coord[0]))
        rots[9].append((+coord[1], -coord[0], +coord[2]))
        rots[10].append((+coord[1], -coord[2], -coord[0]))
        rots[11].append((+coord[1], +coord[0], -coord[2]))
        # negative y
        rots[12].append((-coord[1], -coord[2], +coord[0]))
        rots[13].append((-coord[1], +coord[0], +coord[2]))
        rots[14].append((-coord[1], +coord[2], -coord[0]))
        rots[15].append((-coord[1], -coord[0], -coord[2]))
        # positive z
        rots[16].append((+coord[2], +coord[0], +coord[1]))
        rots[17].append((+coord[2], -coord[1], +coord[0]))
        rots[18].append((+coord[2], -coord[0], -coord[1]))
        rots[19].append((+coord[2], +coord[1], -coord[0]))
        # negative z
        rots[20].append((-coord[2], -coord[0], +coord[1]))
        rots[21].append((-coord[2], +coord[1], +coord[0]))
        rots[22].append((-coord[2], +coord[0], -coord[1]))
        rots[23].append((-coord[2], -coord[1], -coord[0]))
    return rots

    # for x, y, z in scanner:
    #     rots.append((x, y, z))
    #     rots.append((x, -z, y))
    #     ...


if __name__ == '_' \
               '_main__':
    fn = 'day19/input.txt' if input('s(ubmit) else ENTER ') else 'short.txt'
    with open(fn, 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]
