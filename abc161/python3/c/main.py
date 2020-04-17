#!/usr/bin/env python3
# coding: utf-8
# import pprint
# import numpy as np
# import code
# import functools

if __debug__:
    def debug(arg):
        pass
else:
    import sys
    def debug(arg):
        debug = lambda *x: None
        print(arg, file=sys.stderr)

n, k = (int(x) for x in input().split())
debug([n, k])
nn = n - (n // k) * k
debug(nn)
nnn = abs(k - nn)
debug(nnn)
nnnn = min(nn, nnn)
print(nnnn)




