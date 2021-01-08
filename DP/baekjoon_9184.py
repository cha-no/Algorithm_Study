
'''

백준 문제

https://www.acmicpc.net/problem/9184

'''


dp = [[[0]*21 for i in range(21)] for i in range(21)]

for i in range(21):
    dp[i][0][0] = 1
    dp[0][i][0] = 1
    dp[0][0][i] = 1

for i in range(21):
    for j in range(21):
        dp[i][j][0] = 1
        dp[0][i][j] = 1
        dp[j][0][i] = 1

for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i<j and j<k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

while True:
    a, b, c = list(map(int, input().split()))
    if a==-1 and b==-1 and c==-1:
        break
    if a<=0 or b<=0 or c<=0:
        print(f"w({a}, {b}, {c}) = {1}")
    elif a>20 or b>20 or c>20:
        print(f"w({a}, {b}, {c}) = {dp[20][20][20]}")
    else:
        print(f"w({a}, {b}, {c}) = {dp[a][b][c]}")
