
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/67260?language=python3

'''

from typing import List
from collections import deque

def solution(n : int, path : List[List[int]], order : List[List[int]]) -> bool:
    graph = [[] for i in range(n)]
    prior, later, visit = [0] * n, [0] * n, [0] * n
    queue = deque([0])    
    
    for (u, v) in path:
        graph[u].append(v)
        graph[v].append(u)
    
    for i, (u, v) in enumerate(order):
        if not v:
            return False
        prior[v] = u
    
    while queue:
        v = queue.popleft()
        
        if not visit[prior[v]] and not (v == 0 and prior[v] == 0):
            later[prior[v]] = v
            continue
        visit[v] = 1
        
        for u in graph[v]:
            if not visit[u]:
                queue.append(u)
        
        if not visit[later[v]]:
            queue.append(later[v])

    return all(visit)
