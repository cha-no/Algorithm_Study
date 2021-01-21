'''

백준 문제

https://www.acmicpc.net/problem/12865

'''

n, k = list(map(int, input().split()))
items = []

dp = [0]*(k+1)

for i in range(n):
    w, v = list(map(int, input().split()))
    
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[-1])
