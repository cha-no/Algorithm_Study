
'''

백준 문제

https://www.acmicpc.net/problem/1916

'''

import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n)]
for _ in range(m):
    e1, e2, cost = list(map(int, sys.stdin.readline().split()))
    graph[e1 - 1].append((e2, cost))

s, e = list(map(int, sys.stdin.readline().split()))

costs = [100000000 + 1] * n
heap = [(0, s)]

costs[s - 1] = 0
while heap:
    cost, v = heapq.heappop(heap)
    if costs[v - 1] < cost:
        continue
    
    for (u, c) in graph[v - 1]:
        if costs[v - 1] + c < costs[u - 1]:
            costs[u - 1] = costs[v - 1] + c
            heapq.heappush(heap, (costs[u - 1], u))
print(costs[e - 1])
