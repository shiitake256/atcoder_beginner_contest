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

n, m = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
# d = dict.fromkeys(range(1, n), 0)
debug([m, n])
debug(a)

c = 0
t = sum(a)
debug(t)
s = t / (4 * m)
debug(s)
for aa in a:
    if aa >= s:
        c += 1
        if c >= m:
            print('Yes')
            exit()

# debug(c)
print('No')
