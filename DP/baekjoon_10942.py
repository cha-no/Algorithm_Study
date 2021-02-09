'''

백준 문제

https://www.acmicpc.net/problem/10942

'''

import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

dp = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n - i):
        s = j
        e = j + i
        if not i:
            dp[j][i + j] = 1
        elif i == 1:
            if sequence[j] == sequence[i + j]:
                dp[j][i + j] = 1
        else:
            if dp[j + 1][i + j - 1] and sequence[j] == sequence[i + j]:
                dp[j][i + j] = 1

m = int(sys.stdin.readline())
for i in range(m):
    s, e = list(map(int, sys.stdin.readline().split()))
    print(dp[s - 1][e - 1])
