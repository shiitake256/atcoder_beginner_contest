#!/usr/bin/env python3
# coding: utf-8

def debug(arg):
    if __debug__:
        pass
    else:
        import sys
        print(arg, file=sys.stderr)

def main():
    N, K = map(int, open(0).read().split())
    debug([N, K])
    r = N % K
    a = min(r, K - r)
    print(a)

if __name__ == "__main__":
    main()
