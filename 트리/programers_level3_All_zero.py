
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/76503?language=python3#

'''


from typing import List
import sys
sys.setrecursionlimit(300000)

def solution(a : List[int], edges : List[List[int]]) -> int:
    def dfs(v : int, a : List[int], graph : List[List[int]], visit : List[int]) -> int:
        global count
        weight = a[v]
        visit[v] = 1
        for u in graph[v]:
            if not visit[u]:
                w = dfs(u, a, graph, visit)
                weight += w
                count += abs(w)
        return weight
    global count
    count = 0
    visit = [0] * len(a)
    graph = [[] for i in range(len(a))]
    
    for (v1, v2) in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return -1 if dfs(0, a, graph, visit) else count
