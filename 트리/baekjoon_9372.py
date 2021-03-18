
'''

백준 문제

https://www.acmicpc.net/problem/9372

'''

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = list(map(int, sys.stdin.readline().split()))
    for _ in range(m):
        sys.stdin.readline()
    print(n - 1)
