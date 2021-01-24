
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3

'''

import heapq

def solution(N, road, K):
    INF = 500000 + 1
    distance = [INF] * N
    visit = [0] * N
    graph = [[] for i in range(N)]
    heap = []
    
    for edge in road:
        graph[edge[0] - 1].append((edge[1]-1, edge[2]))
        graph[edge[1] - 1].append((edge[0]-1, edge[2]))
    
    distance[0] = 0
    heap.append((0, 0))
    
    while heap:
        dist, v = heapq.heappop(heap)
        visit[v] = 1
        
        for (w, time) in graph[v]:
            if visit[w]:
                continue
            
            if distance[w] > distance[v] + time:
                distance[w] = distance[v] + time
                heapq.heappush(heap, (distance[w], w))
            
    return sum([1 if dist <= K else 0 for dist in distance])
