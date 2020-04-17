#!/usr/bin/env python3
# coding: utf-8
# import pprint
# import numpy as np
# import code
# import functools

# if __debug__:
#     def debug(arg):
#         pass
# else:
#     import sys
#     def debug(arg):
#         debug = lambda *x: None
#         print(arg, file=sys.stderr)

n = int(input())
a = 0
for i in range(1, n + 1):
    if i % 3 != 0 and i % 5 != 0:
        # debug(i)
        a += i
print(a)
