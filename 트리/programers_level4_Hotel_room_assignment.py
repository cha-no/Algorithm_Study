
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/64063?language=python3#

'''
    
    
from typing import List

def solution(k : int, room_number : List[int]) -> List[int]:
    answer = []
    room_dict = {}
    
    for room in room_number:
        visit = []
        root = room
        while root in room_dict:
            visit.append(root)
            root = room_dict[root]
        
        for room in visit:
            room_dict[room] = root
        
        answer.append(root)
        room_dict[root] = root + 1

    return answer
