
'''

백준 문제

https://www.acmicpc.net/problem/1766

'''

import heapq

n, m = map(int, input().split())
m_list = [list(map(int, input().split())) for i in range(m)]

graph = [[] for i in range(n)]
indegree = [0] * n
for a, b in m_list:
    graph[a - 1].append(b - 1)
    indegree[b - 1] += 1

heap = []
for i in range(n):
    if not indegree[i]: heapq.heappush(heap, [0, i])

answer = []
while heap:
    top, u = heapq.heappop(heap)
    answer.append(str(u + 1))

    for v in graph[u]:
        indegree[v] -= 1
        if not indegree[v]: heapq.heappush(heap, [0, v])

print(' '.join(answer))
