# import itertools
# import math
# import functools
# import scipy.special

def debug(arg):
    if __debug__:
        pass
    else:
        import sys
        print(arg, file=sys.stderr)

def exponentiation(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1
    else:
        q, r = divmod(n, 2)
        return exponentiation(a, q) * exponentiation(a, q + r)

n, k = (int(x) for x in input().split())
c = {} 
t = 0
MOD = 1000000007
for x in range(k, 0, -1):
    q = k // x
    c[x] = pow(q, n, MOD) - sum(c[x * y] for y in range(2, q + 1))
    t += c[x] * x
    t = t % MOD
print(t)