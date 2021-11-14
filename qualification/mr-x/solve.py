#!/usr/bin/env python
import sys


def eeval(expr, v):
    ops = {
        '|': lambda x, y: (x | y),
        '&': lambda x, y: (x & y),
        '^': lambda x, y: (x ^ y),
    }

    stack = list()
    for c in expr:
        if c == '(':
            pass
        elif c == ')':
            y = stack.pop()
            op = stack.pop()
            x = stack.pop()
            z = ops[op](x, y)
            stack.append(z)
        elif c == 'x':
            stack.append(v)
        elif c == 'X':
            stack.append(1 - v)
        elif c in '01':
            stack.append(int(c))
        elif c in '|&^':
            stack.append(c)
        else:
            raise Exception(repr(c))
    return stack[-1]


def solver(expr):
    a = eeval(expr, v=0)
    b = eeval(expr, v=1)
    res = 0 if (a == b) else 1
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
        while T > 0:
            T -= 1
            yield (next(fp).strip(), )


if __name__ == '__main__':
    solve(*sys.argv[1:])
