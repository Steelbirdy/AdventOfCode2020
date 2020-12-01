from typing import Callable, Optional


def readlines(path: str, *, fn: Optional[Callable] = None) -> list:
    with open(path, mode='r') as f:
        ret = map(lambda L: L.strip(), f.readlines())
        if fn is not None:
            ret = map(fn, ret)
        return list(ret)
