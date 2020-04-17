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

n = input()
# debug(n)
print('Yes' if any(map(lambda x: x == '7', n)) else "No")