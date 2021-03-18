
'''

프로그래머스 level2 문제

https://programmers.co.kr/learn/courses/30/lessons/42583

'''

from typing import List
from collections import deque

def solution(bridge_length : int, weight : int, truck_weights : List) -> int:
    answer = 0
    truck_weights = deque(truck_weights)
    queue = deque([])
    cur = 0
    
    while True:
        answer += 1
        if queue and answer - queue[0][1] >= bridge_length:
            w, _ = queue.popleft()
            cur -= w

        if truck_weights and cur + truck_weights[0] <= weight:
            truck_weight = truck_weights.popleft()
            queue.append((truck_weight, answer))
            cur += truck_weight
        
        if not queue:
            break
    return answer
