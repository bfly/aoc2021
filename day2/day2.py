with open("input.txt", 'r') as f:
    nums = [line.split() for line in f.readlines()]


def updatePos(dir, v, x, y, aim):
    if dir == "forward":
        return x + v, y + (aim * v), aim
    elif dir == "down":
        return x, y, aim + v
    elif dir == "up":
        return x, y, aim - v


x, y, aim = 0, 0, 0
for dir, v in nums:
    x, y, aim = updatePos(dir, int(v), x, y, aim)

print(f'{x=}, {y=}, {x * y=}')

# 3.10
# def updatePos2(dir,v,x,y,aim):
#     match dir:
#         case "forward":
#             return  x+v, y+(aim*v), aim
#         case "down":
#             return  x, y, aim+v
#         case "up":
#             return x, y, aim-v