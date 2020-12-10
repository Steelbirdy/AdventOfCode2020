from utils import read_input


def part1(data):
    groups = []
    curr = set()
    for line in data:
        line = line.strip(' \n')
        if not line:
            groups.append(curr)
            curr = set()
        else:
            curr |= set(line)
    groups.append(curr)
    return sum(len(g) for g in groups)


def part2(data):
    groups = []
    curr = set(chr(x+97) for x in range(26))
    for line in data:
        line = line.strip(' \n')
        if not line:
            groups.append(curr)
            print(curr)
            curr = set(chr(x+97) for x in range(26))
        else:
            curr &= set(line)
    groups.append(curr)
    return sum(len(g) for g in groups)


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True, fn=None)
    print(part1(data))
    print(part2(data))
