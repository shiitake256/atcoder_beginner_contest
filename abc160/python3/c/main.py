#!/usr/bin/env python3
# coding: utf-8
# import sys
# import pprint
# import numpy as np
# import code
import functools

if __debug__:
    debug = lambda *x: None
else:
    import logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    debug = logger.debug

k, n, *a = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

debug(k)
debug(n)
debug(a)

aa = a.copy()
aa.pop(0)
aa.append(k + a[0])
debug(aa)
# r = functools.reduce(lambda )

d = [y - x for x, y in zip(a,aa)]
debug(d)
d.sort()
debug(d)
d.pop()
debug(d)
print(sum(d))
