#!/usr/bin/env python3
# coding: utf-8
import itertools
import math

if __debug__:
    def debug(arg):
        pass
else:
    import sys
    def debug(arg):
        print(arg, file=sys.stderr)

n = int(input())
c1 = range(1, n + 1)
c2 = itertools.combinations(range(1, n + 1), 2)
c3 = itertools.combinations(range(1, n + 1), 3)

t1 = sum(list(c1))
t2 = sum(list(map(lambda x: math.gcd(x[0], x[1]), c2))) * 6
t3 = sum(list(map(lambda x: math.gcd(x[0], math.gcd(x[1], x[2])), c3))) * 6

debug(t1)
debug(t2)
debug(t3)

print(sum([t1, t2, t3]))