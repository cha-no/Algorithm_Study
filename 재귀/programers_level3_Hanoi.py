
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12946?language=python3

'''

from typing import List

def solution(n : int) -> List[List[int]]:
    def hanoi(n : int, s : int, m : int, e : int) -> List[List[int]]:
        return hanoi(n - 1, s, e, m) + [[s, e]] + hanoi(n - 1, m, s, e) if n != 1 else [[s, e]]
    return hanoi(n, 1, 2, 3)
