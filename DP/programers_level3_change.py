
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12907?language=python3#

'''

def solution(n, money):
    dp = [0] * (n+1)
    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m]
        for i in range(m, n + 1):
            if not i % m:
                dp[i] += 1 
    return dp[n] % 1000000007
