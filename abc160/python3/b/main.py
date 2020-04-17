#!/usr/bin/env python3
# coding: utf-8
# import sys
# import pprint
# import numpy as np
# import code


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

x = int(input())

debug(x)

c500 = int(x / 500)
xx = x % 500
c5 = int(xx / 5)

u = c500 * 1000 + c5 * 5

print(u)

