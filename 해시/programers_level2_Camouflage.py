
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

'''

from typing import List

def solution(clothes : List[List[str]]) -> int:
    answer = 1
    clothes_dict = {}
    for (name, kind) in clothes:
        clothes_dict[kind] = clothes_dict.get(kind, [])
        clothes_dict[kind].append(name)
    
    for v in clothes_dict.values():
        answer *= (1 + len(v))
    
    return answer - 1
