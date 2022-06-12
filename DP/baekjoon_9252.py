
'''

백준 문제

https://www.acmicpc.net/problem/9252

'''

string1, string2 = input(), input()

dp = [[0] * (len(string2) + 1) for i in range(len(string1) + 1)]
traces = [[-1] * (len(string2) + 1) for i in range(len(string1) + 1)]

for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        a = 1 if string1[i - 1] == string2[j - 1] else 0
        if dp[i - 1][j - 1] + a >= dp[i][j - 1] and dp[i - 1][j - 1] + a >= dp[i - 1][j]:
            dp[i][j] = dp[i - 1][j - 1] + a
            traces[i][j] = 0
        elif dp[i][j - 1] >= dp[i - 1][j - 1] + a and dp[i][j - 1] >= dp[i - 1][j]:
            dp[i][j] = dp[i][j - 1]
            traces[i][j] = 1
        elif dp[i - 1][j] >= dp[i - 1][j - 1] + a and dp[i - 1][j] >= dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j]
            traces[i][j] = 2

print(dp[-1][-1])
if dp[-1][-1]:
    i, j = len(string1), len(string2)
    trace = ''
    while traces[i][j] >= 0:
        if traces[i][j] == 0:
            if dp[i - 1][j - 1] != dp[i][j]:
                trace = string2[j - 1] + trace
            i -= 1
            j -= 1
        elif traces[i][j] == 1:
            j -= 1
        elif traces[i][j] == 2:
            i -= 1
    print(trace)
