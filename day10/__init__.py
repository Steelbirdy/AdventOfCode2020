from utils import read_input


def part1(data):
    data = sorted(data)
    ones, threes = int(data[0] == 1), 1+int(data[0] == 3)
    for i, x in enumerate(sorted(data)):
        if i == 0:
            continue
        if x - data[i-1] == 1:
            ones += 1
        elif x - data[i-1] == 3:
            threes += 1
    return ones * threes


def part2(data):
    data.append(max(data)+3)
    data = sorted(data)
    ret = {0: 1}
    for x in data:
        ret[x] = 0
        for d in range(1, 4):
            if x-d not in ret:
                ret[x-d] = 0
            ret[x] += ret[x-d]
    return ret[data[-1]]


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True, fn=int)
    print(part1(data))
    print(part2(data))
