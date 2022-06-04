
'''

백준 문제

https://www.acmicpc.net/problem/11779

'''


import heapq

n, m = int(input()), int(input())
graph = [[] for i in range(n)]

for i in range(m):
    u, v, cost = map(int, input().split())
    graph[u - 1].append((v - 1, cost))

s, e = map(int, input().split())

MAX = n * 100000 + 1
distance = [MAX] * n
distance[s - 1] = 0
before = [-1] * n
heap = [(0, s - 1)]

while heap:
    dist, u = heapq.heappop(heap)
    if dist > distance[u]: continue

    for v, cost in graph[u]:
        if distance[v] > distance[u] + cost:
            distance[v] = distance[u] + cost
            before[v] = u
            heapq.heappush(heap, (distance[u] + cost, v))

print(distance[e - 1])
total = 1
trace = [e]
u = e
while s != u:
    total += 1
    u = before[u - 1] + 1
    trace.append(u)

print(len(trace))
idx = len(trace) - 1
while idx > 0:
    print(trace[idx], end=' ')
    idx -= 1
print(trace[0])
