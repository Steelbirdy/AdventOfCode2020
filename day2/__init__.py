from utils import *


def convert_password_part1(pw: str) -> tuple:
    pw = pw.split(' ', maxsplit=3)
    a, b = pw[0].split('-')
    return (
        range(int(a), int(b)+1),
        pw[1][0],
        pw[2],
    )


def convert_password_part2(pw: str) -> tuple:
    pw = pw.split(' ', maxsplit=3)
    a, b = pw[0].split('-')
    return (
        (int(a), int(b)),
        pw[1][0],
        pw[2],
    )


def is_valid_part1(pw: tuple):
    a, b, c = pw
    a = set(a)
    return sum(1 if k == b else 0 for k in c) in a


def is_valid_part2(pw: tuple):
    a, b, c = pw
    m, M = a
    return (c[m-1] == b) != (c[M-1] == b)


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True)

    # Part 1
    passwords = [convert_password_part1(x) for x in data]
    print(count_matches(passwords, is_valid_part1))

    # Part 2
    passwords = [convert_password_part2(x) for x in data]
    print(count_matches(passwords, is_valid_part2))
