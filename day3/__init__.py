from utils import *


def check_position(data, i: int, slope_y, slope_x):
    return data[slope_y*i][(slope_x*i) % len(data[0])] == '#'


def check_all(data):
    prod = 1
    for slope in ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1)):
        i = 1
        sm = 0
        while slope[0]*i < len(data):
            sm += int(check_position(data, i, *slope))
            i += 1
        prod *= sm
    return prod


if __name__ == '__main__':
    data = read_input('input.txt', fn=None, by_line=True)
    print(check_all(data))
