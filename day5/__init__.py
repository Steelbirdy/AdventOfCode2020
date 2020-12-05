from utils import *


def get_row(val: str) -> int:
    return int(val[:7].replace('F', '0').replace('B', '1'), base=2)


def get_seat(val: str) -> int:
    return int(val[7:].replace('L', '0').replace('R', '1'), base=2)


def get_id(val: str):
    return get_row(val) * 8 + get_seat(val)


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True)
    ids = list(get_id(x) for x in data)
    print('Part 1:', max(ids))
    for id in range(min(ids), max(ids)):
        if id not in ids:
            print('Part 2:', id)
            break
