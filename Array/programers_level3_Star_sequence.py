
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/70130?language=python3

'''

from typing import List

def solution(a : List[int]) -> int:
    def isIndex(i : int, n : int = len(a)) -> bool:
        return i >= 0 and i < n
    
    count = [0] * len(a)
    before = [-1] * len(a)
    
    for i in range(len(a)):
        if isIndex(i) and isIndex(i - 1) and a[i] != a[i - 1] and before[a[i]] != i - 1:
            count[a[i]] += 2
            before[a[i]] = i
        elif isIndex(i + 1) and isIndex(i) and a[i + 1] != a[i]:
            count[a[i]] += 2
            before[a[i]] = i + 1
            
    return max(count)
