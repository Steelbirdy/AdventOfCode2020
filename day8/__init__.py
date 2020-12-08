from utils import read_input


def part1(data):
    i = 0
    accumulator = 0
    done = set()
    while True:
        if i in done:
            return accumulator
        ins, val = data[i]
        done.add(i)
        if ins == 'nop':
            i += 1
            continue
        if ins == 'jmp':
            i += val
            continue
        if ins == 'acc':
            accumulator += val
            i += 1
            continue
        raise ValueError(ins)


def run(data):
    i = 0
    accumulator = 0
    done = set()
    while True:
        if i >= len(data):
            return accumulator
        if i in done:
            return False
        ins, val = data[i]
        done.add(i)
        if ins == 'nop':
            i += 1
            continue
        if ins == 'jmp':
            i += val
            continue
        if ins == 'acc':
            accumulator += val
            i += 1
            continue
        raise ValueError(ins)


def part2(data):
    d = data.copy()
    for n in range(len(data)):
        ins, val = d[n]
        if ins == 'nop':
            d[n] = ('jmp', val)
        elif ins == 'jmp':
            d[n] = ('nop', val)
        else:
            continue
        acc = run(d)
        if acc is not False:
            return acc
        else:
            d = data.copy()


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True, fn=lambda x: (lambda y: (y[0], int(y[1])))(x.split(' ')))
    print(part1(data))
    print(part2(data))
