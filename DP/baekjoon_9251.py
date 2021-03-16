
'''

백준 문제

https://www.acmicpc.net/problem/9251

'''

s1 = input()
s2 = input()

n1 = len(s1)
n2 = len(s2)

dp = [[0] * (n1 + 1) for i in range(n2 + 1)]

for j in range(1, n1 + 1):
    for i in range(1, n2 + 1):
        if s1[j - 1] == s2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
