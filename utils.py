from typing import Callable, Optional


def read_input(path: str, *, by_line: bool, fn: Optional[Callable] = None) -> list:
    with open(path, mode='r') as f:
        ret = map(lambda L: L.strip(), f.readlines())
        if by_line is not True:
            ret = list(ret)[0].split(',')
        if fn is not None:
            ret = map(fn, ret)
        return list(ret)


def count_matches(iter, fn: Callable) -> int:
    # return len(filter(fn, iter))
    return sum(1 if fn(x) else 0 for x in iter)
