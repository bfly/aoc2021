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


def parse_operator(bits):
    res = ""
    if bits[0] == "0":  # 15 bit num which says how long the subpackets are in total
        bits = bits[16:]
    elif bits[0] == "1":  # how many subpackets
        subpackets_num = int(bits[1:12], 2)
        bits = bits[12:]
        for _ in range(subpackets_num):
            res_n, bits = parse_packet(bits)
            res += res_n

    return res, bits


def parse_packet(bits):
    global version_sum
    if bits.count("0") == len(bits):  # end
        return "", ""
    version = bits[:3]
    version_sum += int(version, 2)
    type_id = bits[3:6]
    bits = bits[6:]
    res, bits = parse_literal(bits) if type_id == "100" else parse_operator(bits)
    return res, bits


version_sum = 0
while binary:
    _, binary = parse_packet(binary)

print(f'{version_sum=}')

