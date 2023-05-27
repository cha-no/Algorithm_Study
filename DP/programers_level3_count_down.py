
'''

프로그래머스 level3 문제

https://school.programmers.co.kr/learn/courses/30/lessons/131129

'''


from typing import List

INF = 100000 + 1

SCORE_DICT = {
    1: True, 
    2: True, 
    3: True, 
    4: True, 
    5: True, 
    6: True, 
    7: True, 
    8: True, 
    9: True, 
    10: True, 
    11: True, 
    12: True, 
    13: True, 
    14: True, 
    15: True, 
    16: True, 
    17: True, 
    18: True, 
    19: True, 
    20: True, 
    21: False, 
    22: False, 
    24: False, 
    26: False, 
    27: False, 
    28: False, 
    30: False, 
    32: False, 
    33: False, 
    34: False, 
    36: False, 
    38: False, 
    39: False, 
    40: False, 
    42: False, 
    45: False, 
    48: False, 
    50: True, 
    51: False, 
    54: False, 
    57: False, 
    60: False, 
}

def solution(target: int) -> List[int]:
    count_dp = [INF] * (target + 1)
    good_dp = [0] * (target + 1)

    for target_score in range(1, target + 1):
        for score, flag in SCORE_DICT.items():
            if target_score == score:
                count_dp[target_score] = 1
                if flag: good_dp[target_score] = 1
                else: good_dp[target_score] = 0
            else:
                diff_score = target_score - score
                if diff_score > 0:
                    temp = count_dp[diff_score]
                    plus_good = 1 if flag else 0
                    if temp + 1 == count_dp[target_score]:
                        good_dp[target_score] = max(good_dp[target_score], plus_good + good_dp[diff_score])
                    elif temp + 1 < count_dp[target_score]:
                        count_dp[target_score] = temp + 1
                        good_dp[target_score] = plus_good + good_dp[diff_score]
    
    return [count_dp[target], good_dp[target]]
