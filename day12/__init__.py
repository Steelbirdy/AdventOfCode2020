from utils import read_input


def rotate(facing, d, v):
    left = {'N': 'W', 'S': 'E', 'W': 'S', 'E': 'N'}
    right = {'W': 'N', 'E': 'S', 'S': 'W', 'N': 'E'}
    for _ in range(v // 90):
        if d == 'L':
            facing = left[facing]
        elif d == 'R':
            facing = right[facing]
    return facing


def part1(data):
    facing = 'E'
    delta = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
    x, y = 0, 0
    for (d, v) in data:
        if d in 'LR':
            facing = rotate(facing, d, v)
        elif d == 'F':
            x += delta[facing][0] * v
            y += delta[facing][1] * v
        else:
            x += delta[d][0] * v
            y += delta[d][1] * v
    return abs(x) + abs(y)


def part2(data):
    delta = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
    x, y = 0, 0
    wx, wy = 10, 1
    for (d, v) in data:
        if d == 'L':
            for _ in range(v // 90):
                wx, wy = -wy, wx
        elif d == 'R':
            for _ in range(v // 90):
                wx, wy = wy, -wx
        elif d == 'F':
            x += wx * v
            y += wy * v
        else:
            wx += delta[d][0] * v
            wy += delta[d][1] * v
    return abs(x) + abs(y)


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True, fn=lambda x: (x[0], int(x[1:])))
    print(part1(data))
    print(part2(data))
