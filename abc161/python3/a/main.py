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

ｘ, y, z = (int(x) for x in input().split())
debug([x, y, z])

a = z
b = x
c = y

print(' '.join(map(str, [a, b, c])))
