from utils import read_input


def part1(data):
    for i, x in enumerate(data[25:], start=25):
        prev = set(data[i-25:i])
        found = None
        for y in prev:
            if x - y in prev:
                found = y
                break
        if found is None:
            return x
    return False


def is_invalid(x, prev):
    found = False
    for y in set(prev):
        if x - y in prev:
            found = y
            break
    return found


def part2(data):
    VALUE = 57195069
    for size in range(2, len(data)):
        for i in range(len(data) - size):
            if sum(data[i:i+size]) == VALUE:
                print(data[i:i+size])
                return max(data[i:i+size]) + min(data[i:i+size])
    return False


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True, fn=int)
    print(part1(data))
    print(part2(data))
