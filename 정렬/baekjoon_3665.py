
'''

백준 문제

https://www.acmicpc.net/problem/3665

'''

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    m_list = [list(map(int, input().split())) for i in range(m)]

    graph = [[] for i in range(n)]
    indegree = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            graph[t[i] - 1].append(t[j] - 1)
            indegree[t[j] - 1] += 1

    for u, v in m_list:
        if v - 1 in graph[u - 1]:
            indegree[u - 1] += 1
            indegree[v - 1] -= 1
            graph[u - 1].remove(v - 1)
            graph[v - 1].append(u - 1)
        else:
            indegree[u - 1] -= 1
            indegree[v - 1] += 1
            graph[u - 1].append(v - 1)
            graph[v - 1].remove(u - 1)

    answer = []
    imp_flag = False
    queue = deque([])
    for i in range(n):
        if not indegree[i]: queue.append(i)

    for i in range(n):
        if not queue: 
            imp_flag = True
            break
        u = queue.popleft()
        answer.append(str(u + 1))

        for v in graph[u]:
            indegree[v] -= 1
            if not indegree[v]: queue.append(v)

    if imp_flag: print("IMPOSSIBLE")
    else: print(' '.join(answer))
