
'''

백준 문제

https://www.acmicpc.net/problem/11053

'''

n = int(input())
a = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    m = 0
    for j in range(i):
        if a[i] > a[j]:
            m = max(m, dp[j])
    dp[i] = m + 1

print(max(dp))
