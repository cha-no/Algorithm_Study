
'''

프로그래머스 level3 문제

https://school.programmers.co.kr/learn/courses/30/lessons/138475?language=python3

'''


from typing import List

def solution(e: int, starts: List[int]) -> List[int]:
    factors = [1] * (e + 1)
    dp = [e] * (e + 1)
    for gap in range(2, e + 1):
        for n in range(gap, e + 1, gap):
            factors[n] += 1
    
    max_num = factors[e]
    for n in range(e - 1, min(starts) - 1, -1):
        if factors[n] >= max_num:
            dp[n] = n
            max_num = factors[n]
        else:
            dp[n] = dp[n + 1]
    return [dp[n] for n in starts]
