
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/12983?language=python3

'''



from typing import List

def solution(strs : List[str], t : str) -> int:
    INF = 20000 + 1
    dp = [0] + [INF] * len(t)
    end_dict = {}
    
    for tgt in set(t):
        end_dict[tgt] = []
        for s in strs:
            if s[-1] == tgt:
                end_dict[tgt].append(s)
        
    for i, tgt in enumerate(t, start=1):
        for s in end_dict[tgt]:
            if t[i-len(s):i] == s:
                dp[i] = min(dp[i], dp[i-len(s)] + 1)

    return -1 if dp[-1] == INF else dp[-1]
