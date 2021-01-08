
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3

'''


def solution(m, n, puddles):
    dp = [[0]*m for i in range(n)]
    
    for i in range(n):
        if [1,i+1] in puddles:
            break
        dp[i][0] = 1
    for j in range(m):
        if [j+1,1] in puddles:
            break
        dp[0][j] = 1
    
    for i in range(1,n):
        for j in range(1,m):
            if [j+1,i+1] not in puddles:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[-1][-1] % 1000000007
