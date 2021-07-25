
'''

백준 문제

https://www.acmicpc.net/problem/2293

'''


n, k = list(map(int, input().split()))
coins = [int(input()) for i in range(n)]

dp = {0: 0}
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = dp.get(i, 0) + dp.get(i - coin, 0)
    for i in range(coin, k + 1):
        if not i % coin:
            dp[i] += 1

print(dp[k])
