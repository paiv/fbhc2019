#!/usr/bin/env python
import sys


def solver(pond):
    b = pond.count('B')
    n = len(pond) - 1
    res = (b < n) and (2 * b >= n)
    return 'Y' if res else 'N'


def solve(fn):
    for index, args in enumerate(parse(fn), 1):
        print(f'Case #{index}: ', end='', flush=True)
        res = solver(*args)
        print(res, flush=True)


def parse(fn):
    state = 0
    with open(fn) as fp:
        T = int(next(fp), 10)
        while T > 0:
            T -= 1
            yield (next(fp).strip(), )


if __name__ == '__main__':
    solve(*sys.argv[1:])
