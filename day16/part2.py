f = open("input.txt").read().strip()
binary = "".join([bin(int(x, 16))[2:].zfill(4) for x in f])


def parse_literal(bits):
    res = ""
    while True:
        num = bits[:5]
        bits = bits[5:]
        res += num[1:]
        if num[0] == "0":  # last
            return res, bits


def parse_operator(bits, type_id):
    if bits[0] == "0":  # 15 bit num which says how long the subpackets are in total
        subpackets_len = int(bits[1:16], 2)
        bits = bits[16:]
        res, _ = parse_packet(bits[:subpackets_len], list())
        bits = bits[subpackets_len:]
    elif bits[0] == "1":  # how many subpackets
        subpackets_num = int(bits[1:12], 2)
        bits = bits[12:]
        res = []
        for _ in range(subpackets_num):
            res_n, bits = parse_packet(bits, list(), single=True)
            res.append(res_n)

    res = [int(x, 2) for x in res]
    type_id = int(type_id, 2)
    if type_id == 0:
        out = sum(res)
    elif type_id == 1:
        out = 1
        for x in res:
            out *= x
    elif type_id == 2:
        out = min(res)
    elif type_id == 3:
        out = max(res)
    elif type_id == 5:
        out = int(res[0] > res[1])
    elif type_id == 6:
        out = int(res[1] > res[0])
    elif type_id == 7:
        out = int(res[0] == res[1])
    return bin(out)[2:], bits


def parse_packet(bits, res, single=False):
    if bits.count("0") == len(bits):
        return res, ""
    type_id = bits[3:6]
    bits = bits[6:]
    if type_id == "100":
        res_n, bits = parse_literal(bits)
    else:
        res_n, bits = parse_operator(bits, type_id)
    res.append(res_n)
    if single:
        return res[0], bits
    return parse_packet(bits, res)


res = parse_packet(binary, list())[0]
print('Expression:', int(res[0], 2))