'''

백준 문제

https://www.acmicpc.net/problem/11049

'''

import sys

n = int(sys.stdin.readline())

mats = []
for i in range(n):
    mats.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*n for i in range(n)]

for i in range(1, n):
    for j in range(n-i):
        for k in range(j, i+j):
            temp = dp[j][k] + dp[k+1][i+j] + mats[j][0]*mats[k][1]*mats[i+j][1]
            dp[j][i+j] = min(dp[j][i+j], temp) if dp[j][i+j] else temp
print(dp[0][n-1])
