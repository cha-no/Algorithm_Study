
'''

백준 문제

https://www.acmicpc.net/problem/2805

'''

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

s, e = 1, 10**9
answer = 0

while s <= e:
    m = (s + e) // 2
    h = sum([(tree - m) if tree >= m else 0 for tree in trees])
    if h >= M:
        answer = max(answer, m)
        s = m + 1
    else:
        e = m - 1
print(answer)
