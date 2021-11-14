#!/usr/bin/env python
import sys


def solver(N, rules):
    print(N)
    print(repr(rules))
    res = 0
    return res


def solve(fn):
    for index, args in enumerate(parse(fn), 1):
        print(f'Case #{index}: ', end='', flush=True)
        res = solver(*args)
        print(res, flush=True)


def parse(fn):
    state = 0
    with open(fn) as fp:
        T = int(next(fp), 10)
        for _ in range(T):
            N, M = map(int, next(fp).split())
            rules = [tuple(map(int, next(fp).split()))
                for _ in range(M)]
            yield (N, rules)


if __name__ == '__main__':
    solve(*sys.argv[1:])
