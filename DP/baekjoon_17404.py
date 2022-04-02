
'''

백준 문제

https://www.acmicpc.net/problem/17404

'''

MAX = 1001 ** 2 + 1

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
dp = [[MAX] * 3 for _ in range(n)]
answer = MAX

for i in range(3):
    for j in range(3):
        if i == j: dp[0][j] = costs[0][j]
        else: dp[0][j] = MAX
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + costs[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + costs[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + costs[j][2]
    for j in range(3):
        if i == j: continue
        answer = min(answer, dp[-1][j])
print(answer)
