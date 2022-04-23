
'''

백준 문제

https://www.acmicpc.net/problem/9370

'''

from typing import List
import heapq

INF = 50000000 + 1

def dijkstra(start: int, n: int) -> List[int]:
    distance = [INF] * n
    distance[start - 1] = 0
    visit = [False] * n
    
    heap = []
    heapq.heappush(heap, (0, start - 1))

    while heap:
        cost, u = heapq.heappop(heap)
        if visit[u]: continue

        visit[u] = True
        for edge in vertex_to_edge[u]:
            v, w, cost = edges[edge]
            if u == w:
                w = v
            if distance[u] + cost < distance[w]:
                distance[w] = distance[u] + cost
                heapq.heappush(heap, (distance[w], w))
    
    return distance

def is_path(dest: int) -> bool:
    if (distance_s[dest - 1] == distance_s[g - 1] + distance_g[h - 1] + distance_h[dest - 1]): return True
    elif (distance_s[dest - 1] == distance_s[h - 1] + distance_h[g - 1] + distance_g[dest - 1]): return True
    else: return False

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())

        edges = []
        vertex_to_edge = [[] for i in range(n)]

        for i in range(m):
            u, v, cost = map(int, input().split())
            edges.append([u - 1, v - 1, cost])
            vertex_to_edge[u - 1].append(i)
            vertex_to_edge[v - 1].append(i)

        dests = [int(input()) for i in range(t)]

        distance_s = dijkstra(s, n)
        distance_g = dijkstra(g, n)
        distance_h = dijkstra(h, n)

        answer = [dest for dest in dests if is_path(dest)]
        print(' '.join(map(str, sorted(answer))))
