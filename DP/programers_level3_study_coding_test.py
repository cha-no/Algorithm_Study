
'''

프로그래머스 level3 문제

https://school.programmers.co.kr/learn/courses/30/lessons/118668

'''



from typing import List

def solution(alp: int, cop: int, problems: List[List[int]]) -> int:
    MAX = 151
    COST_MAX = 301
    dp = [[COST_MAX] * MAX for _ in range(MAX)]
    problems.extend([[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]])

    max_alp = alp
    max_cop = cop
    for problem in problems:
        alp_req, cop_req, _, _, _ = problem
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    next_i = min(i + alp_rwd, max_alp)
                    next_j = min(j + cop_rwd, max_cop)
                    dp[next_i][next_j] = min(dp[next_i][next_j], dp[i][j] + cost)
    return dp[max_alp][max_cop]
