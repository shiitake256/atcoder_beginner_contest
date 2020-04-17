#!/usr/bin/env python3
# coding: utf-8
def debug(arg):
    if __debug__:
        pass
    else:
        import sys
        print(arg, file=sys.stderr)

n = int(input())
s = []
r, g, b = [0] * 3
for c in input():
    if c == 'R':
        s.append(0)
        r += 1
    elif c == 'G':
        s.append(1)
        g += 1
    else:
        s.append(2)
        b += 1

c = r * g * b
for i in range(n):
    for j in range(i + 1, n):
        k = j + (j - i)
        if k < n and s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
            c -= 1

print(c)