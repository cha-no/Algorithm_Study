
'''

백준 문제

https://www.acmicpc.net/problem/11780

'''


n, m = int(input()), int(input())
graph = [[100000 + 1] * n for i in range(n)]
trace = [[[] for j in range(n)] for i in range(n)]

for i in range(n):
    graph[i][i] = 0
for i in range(m):
    u, v, cost = map(int, input().split())
    graph[u - 1][v - 1] = min(graph[u - 1][v - 1], cost)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist = graph[i][k] + graph[k][j]
            if dist < graph[i][j]:
                t1 = trace[i][k]
                t2 = trace[k][j]
                trace[i][j] = []
                for t in t1:
                    trace[i][j].append(t)
                trace[i][j].append(k + 1)
                for t in t2:
                    trace[i][j].append(t)
                graph[i][j] = dist

for t in graph:
    t = [i if i != 100000 + 1 else 0 for i in t]
    print(' '.join(map(str, t)))

for i in range(n):
    for j in range(n):
        if i == j or graph[i][j] == 100000 + 1: print(0)
        else:
            print(len(trace[i][j]) + 2, end=' ')
            print(i + 1, end=' ')
            for t in trace[i][j]:
                print(t, end=' ')
            print(j + 1, end='\n')
