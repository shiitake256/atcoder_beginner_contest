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

s = input()
debug(s[2])

print('Yes' if s[2] == s[3] and  s[4] == s[5] else 'No')
