
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/81304?language=python3#

'''



from typing import List
import heapq

def solution(n : int, start : int, end : int, roads : List[List[int]], traps : List[int]) -> int:
    answer = 2 * 3000 ** 2 + 1
    graph = [[] for i in range(n)]
    dist = {v: {} for v in range(n)}
    heap = [(0, start - 1, 0)]

    for (i, road) in enumerate(roads):
        p, q, s = road
        graph[p - 1].append(i)
        graph[q - 1].append(i)
    
    while heap:
        time, u, bit_mask = heapq.heappop(heap)

        if u + 1 == end:
            answer = min(answer, time)
            continue
        
        if time > answer:
            continue
        
        if u + 1 in traps:
            for e in graph[u]:
                if bit_mask & (1 << e):
                    bit_mask = bit_mask & ~(1 << e)
                else:
                    bit_mask = bit_mask | (1 << e)
        
        if bit_mask not in dist[u] or time < dist[u][bit_mask]:
            dist[u][bit_mask] = time
            for e in graph[u]:
                if bit_mask & (1 << e):
                    if roads[e][1] == u + 1:
                        heapq.heappush(heap, (time + roads[e][2], roads[e][0] - 1, bit_mask))
                else:
                    if roads[e][0] == u + 1:
                        heapq.heappush(heap, (time + roads[e][2], roads[e][1] - 1, bit_mask))
    
    return answer
