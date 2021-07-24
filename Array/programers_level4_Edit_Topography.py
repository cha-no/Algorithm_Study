
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/12984?language=python3

'''


from typing import List

def solution(land : List[List[int]], P : int, Q : int) -> int:
    before = 0    
    total = 0
    square = len(land) ** 2
    poss = set()
    count_dict = {}
    
    for i in land:
        for j in i:
            total += j
            count_dict[j] = count_dict.get(j, 0) + 1
            poss.add(j)
    
    poss = sorted(poss)
    p, q = 0, total
    answer = q * Q
    
    for i in range(len(poss)):
        p += len(land) ** 2 * (poss[i] - before) - square * (poss[i] - before)
        q -= square * (poss[i] - before)
        answer = min(answer, q * Q + p * P)
        before = poss[i]
        square -= count_dict[poss[i]]
    
    return answer
