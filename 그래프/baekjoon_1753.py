'''

백준 문제

https://www.acmicpc.net/problem/1753

'''

import sys
import heapq

v, e = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline())

edges = []
for i in range(e):
    edges.append(list(map(int, sys.stdin.readline().split())))

INF = 987654321
graph = [[] for i in range(v)]
distance = [INF]*v
visit = [0]*v
heap = []

distance[s-1] = 0
for edge in edges:
    graph[edge[0]-1].append((edge[1]-1, edge[2]))

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

for cost in distance:
    if cost==INF:
        print('INF')
    else:
        print(cost)
