from utils import read_input


def part1(data):
    last = {x: i for (i, x) in enumerate(data)}
    n = 6
    L = 6
    while L < 2020:
        if n not in last:
            last[n] = L - 1
            n = 0
            L += 1
        else:
            nx = L - 1 - last[n]
            last[n] = L - 1
            L += 1
            n = nx
    return n


def part2(data):
    last = {x: i for (i, x) in enumerate(data)}
    n = 6
    L = 6
    while L < 30000000:
        if n not in last:
            last[n] = L - 1
            n = 0
            L += 1
        else:
            nx = L - 1 - last[n]
            last[n] = L - 1
            L += 1
            n = nx
    return n


if __name__ == '__main__':
    data = [2, 1, 10, 11, 0, 6]
    print(part1(data))
    print(part2(data))
