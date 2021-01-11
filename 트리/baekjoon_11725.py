'''

백준 문제

https://www.acmicpc.net/problem/11725

'''

n = int(input())

graph = [[] for i in range(n)]
visit = [0]*n
par = {}
stack = [0]

for i in range(n-1):
    u, v = list(map(int, input().split()))
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visit[0] = 1
while stack:
    v = stack.pop()
    for u in graph[v]:
        if visit[u]:
            continue
        visit[u] = 1
        par[u] = v
        stack.append(u)

for i in range(1, n):
    print(par[i]+1)
