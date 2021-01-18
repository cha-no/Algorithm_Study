'''

백준 문제

https://www.acmicpc.net/problem/1504

'''

import sys
import heapq

def dijkstra(s):
    distance = [INF]*n
    visit = [0]*n
    heap = []

    distance[s-1] = 0
    heapq.heappush(heap,(0, s-1))

    while heap:
        d, u = heapq.heappop(heap)
        if visit[u]:
            continue

        visit[u] = 1
        for (w, cost) in graph[u]:
            if distance[u] + cost < distance[w]:
                distance[w] = distance[u] + cost
                heapq.heappush(heap, (distance[w], w))
                
    return distance

if __name__ == "__main__":
    INF = 987654321
    n, e = list(map(int, sys.stdin.readline().split()))
    graph = [[] for i in range(n)]

    for i in range(e):
        u, v, cost = list(map(int, sys.stdin.readline().split()))
        graph[u-1].append((v-1, cost))
        graph[v-1].append((u-1, cost))

    must = list(map(int, sys.stdin.readline().split()))

    start = dijkstra(1)
    must1 = dijkstra(must[0])
    must2 = dijkstra(must[1])
    
    answer = min(start[must[0]-1] + must2[n-1] + must1[must[1]-1], start[must[1]-1] + must1[n-1] + must2[must[0]-1])
    if answer >= INF:
        print(-1)
    else:
        print(answer)
