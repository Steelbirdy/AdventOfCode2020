from utils import read_input


def part1(data):
    print(data[0])
    t0 = int(data[0].strip(' \n'))
    buses = [int(b) for b in data[1].strip(' \n').split(',') if b != 'x']
    min_bus = min(buses, key=lambda b: b - (t0 % b))
    return min_bus * (min_bus - (t0 % min_bus))


def part2(data):
    buses = list(enumerate(data[1].strip(' \n').split(',')))
    buses = list((x, int(y)) for (x, y) in filter(lambda x: x[1] != 'x', buses))
    ret = ', '.join(f'(t+{x}) mod {y} = 0' for (x, y) in buses)
    return 'Punch this into Wolfram Alpha: ' + ret


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True)
    print(part1(data))
    print(part2(data))
