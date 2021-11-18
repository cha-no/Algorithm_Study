
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/86053?language=python3

'''

from typing import List

def isPossible(a : int, b : int, maxGold : int, maxSilver : int, minSilver : int) -> bool:
    return a <= maxGold and b <= maxSilver and a + b <= maxGold + minSilver

def solution(a : int, b : int, g : List[int], s : List[int], w : List[int], t : List[int]) -> int:
    start, end = 1, 4 * 10e14 + 1
    answer = end
    while start <= end:
        mid = (start + end) // 2
        maxGold, minSilver = 0, 0
        minGold, maxSilver = 0, 0
        for (gold, silver, weight, time) in zip(g, s, w, t) :
            trip = ((mid // time) + 1) // 2
            amount1 = weight * trip
            amount2 = weight * trip
            if gold > 0:
                goldAmount = min(gold, amount1)
                amount1 -= goldAmount
                maxGold += goldAmount
            if silver > 0:
                silverAmount = min(silver, amount1)
                minSilver += silverAmount
                silverAmount = min(silver, amount2)
                amount2 -= silverAmount
                maxSilver += silverAmount
            if gold > 0:
                goldAmount = min(gold, amount2)
                minGold += goldAmount
        if isPossible(a, b, maxGold, maxSilver, minSilver):
            answer = min(answer, mid)
            end = mid - 1
        else :
            start = mid + 1
    return answer
