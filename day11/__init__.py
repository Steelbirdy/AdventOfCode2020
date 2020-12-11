from utils import read_input
import numpy as np


d = {(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)}


def adjacent1(x, y, data):
    ret = set()
    shape = data.shape
    for (dx, dy) in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < shape[0] and 0 <= ny < shape[1]:
            ret.add((dx, dy))
    return ret


def adjacent2(x, y, data):
    ret = set()
    shape = data.shape
    for (dx, dy) in d:
        nx, ny = x+dx, y+dy
        while 0 <= nx < shape[0] and 0 <= ny < shape[1] and data[nx, ny] == 0:
            nx += dx
            ny += dy
        if 0 <= nx < shape[0] and 0 <= ny < shape[1]:
            ret.add((nx, ny))
    return ret


def apply1(data):
    ret = np.ndarray(data.shape, dtype=np.int_)
    shape = data.shape
    for x in range(shape[0]):
        for y in range(shape[1]):
            if data[x, y] == 2 and not any(data[x+t[0], y+t[1]] == 1 for t in adjacent1(x, y, data)):
                ret[x, y] = 1
            elif data[x, y] == 1 and sum(data[x+t[0], y+t[1]] == 1 for t in adjacent1(x, y, data)) >= 4:
                ret[x, y] = 2
            else:
                ret[x, y] = data[x, y]
    return ret


def apply2(data):
    ret = np.ndarray(data.shape, dtype=np.int_)
    shape = data.shape
    for x in range(shape[0]):
        for y in range(shape[1]):
            if data[x, y] == 2 and not any(data[t[0], t[1]] == 1 for t in adjacent2(x, y, data)):
                ret[x, y] = 1
            elif data[x, y] == 1 and sum(data[t[0], t[1]] == 1 for t in adjacent2(x, y, data)) >= 5:
                ret[x, y] = 2
            else:
                ret[x, y] = data[x, y]
    return ret


def part1(data):
    A = np.array(data, dtype=np.int_)
    last = np.array(A)
    A = apply1(A)
    while not (A == last).all():
        last = A
        A = apply1(A)
    return np.sum(A == 1)


def part2(data):
    A = np.array(data, dtype=np.int_)
    last = np.array(A)
    A = apply2(A)
    while not (A == last).all():
        last = A
        A = apply2(A)
    return np.sum(A == 1)


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True, fn=lambda x: x.strip(' \n').replace('L', '2').replace('.', '0').replace('#', '1'))
    data = list(map(lambda x: list(map(int, x)), data))
    print(part1(data))
    print(part2(data))
