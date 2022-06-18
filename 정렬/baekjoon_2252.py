
'''

백준 문제

https://www.acmicpc.net/problem/2252

'''

from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n)]
indegree = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    indegree[v - 1] += 1

answer = []
queue = deque([])
for i in range(n):
    if not indegree[i]: queue.append(i)

for i in range(n):
    if not queue:
        raise Exception("사이클이 있어요")
    
    u = queue.popleft()
    answer.append(str(u + 1))
    
    for v in graph[u]:
        indegree[v] -= 1
        if not indegree[v]: queue.append(v)
print(' '.join(answer))
