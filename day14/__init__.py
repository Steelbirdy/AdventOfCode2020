from utils import read_input


def apply_mask(n, mask):
    ret = ''
    b = bin(n)[2:]
    for i, c in enumerate(reversed(mask), start=1):
        if c == 'X':
            if len(b) >= i:
                ret = b[-i] + ret
            else:
                ret = '0' + ret
        else:
            ret = c + ret
    return int(ret, base=2)


def apply_mask2(n, mask):
    ret = ''
    floating = set()
    b = bin(n)[2:]
    for i, c in enumerate(reversed(mask), start=1):
        if c == '0':
            if len(b) >= i:
                ret = b[-i] + ret
            else:
                ret = '0' + ret
        elif c == '1':
            ret = '1' + ret
        else:
            floating.add(i)
            ret = 'X' + ret
    ret = [ret]
    for _ in floating:
        L = len(ret)
        for j in range(L):
            ret.append(ret[j].replace('X', '0', 1))
            ret.append(ret[j].replace('X', '1', 1))
        ret = ret[L:]
    return [int(x, base=2) for x in ret]


def part1(data):
    mask = None
    mem = dict()
    for (var, val) in data:
        if var == 'mask':
            mask = val
        else:
            res = apply_mask(int(val), mask)
            mem[int(var[4:-1])] = res
    return sum(mem.values())


def part2(data):
    mask = None
    mem = dict()
    for (var, val) in data:
        if var == 'mask':
            mask = val
        else:
            addresses = apply_mask2(int(var[4:-1]), mask)
            for add in addresses:
                mem[add] = int(val)
    return sum(mem.values())


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True, fn=lambda x: (lambda y: [y[0], y[2]])(x.strip(' \n').split(' ')))
    print(part1(data))
    print(part2(data))
