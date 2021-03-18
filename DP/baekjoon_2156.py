
'''

백준 문제

https://www.acmicpc.net/problem/2156

'''

n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = wine[0]
if n > 1:
    dp[1] = wine[1] + dp[0]
if n > 2:
    dp[2] = max(wine[2] + max(dp[0], wine[1]), dp[1])
if n > 3:
    dp[3] = max(wine[3] + max(dp[1], wine[2] + dp[0]), dp[2])

for i in range(4, n):
    dp[i] = max(wine[i] + max(dp[i - 2], wine[i - 1] + dp[i - 3], wine[i - 1] + dp[i - 4]), dp[i - 1])

print(dp[-1])
