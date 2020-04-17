#!/usr/bin/env python3
# coding: utf-8
# import pprint
# import numpy as np
# import code
import functools

if __debug__:
    def debug(arg):
        pass
else:
    import sys
    def debug(arg):
        debug = lambda *x: None
        print(arg, file=sys.stderr)

n, x, y = (int(x) for x in input().split())
d = dict.fromkeys(range(1, n), 0)
debug(d)
for i in range(1, n):
    for j in range(i + 1, n + 1):
        debug([i, j, x, y])
        dd1=abs(x - i) + 1 + abs(y - j)
        dd2= j - i
        if dd1 < dd2:
            d[dd1] += 1
        else:
            d[dd2] += 1
        debug(d)

for n in d.values():
    print(n)
