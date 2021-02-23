
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/60061

'''

from typing import List

def solution(n : int, build_frame : List[List[int]]) -> List[List[int]]:
    def isInstall(x : int, y : int, a : int, b : int = 1, n : int = n) -> bool:
        poss = False
        if a:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                poss = True
        else:
            if not y or [x, y - 1, 0] in answer or [x, y, 1] in answer or [x - 1, y, 1] in answer:
                poss = True
        return poss

    answer = []
    for (x, y, a, b) in build_frame:
        if b and isInstall(x, y, a):
            answer.append([x, y, a])
        elif not b:
            answer.remove([x, y, a])
            for bulid in answer:
                if not isInstall(*bulid):
                    answer.append([x, y, a])
                    break

    return sorted(answer)
