'''

백준 문제

https://www.acmicpc.net/problem/1260

'''

from collections import deque

n, m, v = list(map(int, input().split()))

graph = [[0] * n for i in range(n)]

for i in range(m):
    u, w = list(map(int, input().split()))
    graph[u - 1][w - 1] = 1
    graph[w - 1][u - 1] = 1

answer = []
stack = [v]
visit = [0] * n

while stack:
    u = stack.pop()
    if visit[u - 1]:
        continue

    visit[u - 1] = 1
    answer.append(str(u))
    for i in range(n - 1, -1, -1):
        if visit[i] or not graph[u - 1][i]:
            continue
        if graph[u - 1][i]:
            stack.append(i + 1)

print(' '.join(answer))

answer = []        
queue = deque([v])
visit = [0] * n
visit[v - 1] = 1

while queue:
    u = queue.popleft()
    answer.append(str(u))

    for i in range(n):
        if visit[i] or not graph[u - 1][i]:
            continue
        if graph[u - 1][i]:
            queue.append(i + 1)
            visit[i] = 1
            
print(' '.join(answer))
