#!/usr/bin/env python3
# coding: utf-8
import math
import itertools
import collections

# def debug(arg):
#     if __debug__:
#         pass
#     else:
#         import sys
#         print(arg, file=sys.stderr)

def main():
    K = int(input())
    print(next(itertools.islice(lunlun(), K - 1, None)))

def lunlun():
    q = collections.deque(range(1,10))
    while True:
        x = q.popleft()
        yield x
        r = x % 10
        if r != 0:
            q.append(10 * x + r - 1)
        q.append(10 * x + r)
        if r != 9:
            q.append(10 * x + r + 1)

if __name__ == "__main__":
    main()