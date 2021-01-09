'''

백준 문제

https://www.acmicpc.net/problem/11066

'''


INF = 500*500*10000+1
n = int(input())

for t in range(n):
    m = int(input())
    file = list(map(int, input().split()))
    s = [0]*(m+1)
    dp = [[0]*m for i in range(m)]

    for i in range(1,m+1):
        s[i] = s[i-1] + file[i-1]

    for i in range(1,m):
        for j in range(m-i):
            dp[j][i+j] = INF
            for k in range(j, j+i):
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + s[j+i+1] - s[j])
    print(dp[0][m-1])
