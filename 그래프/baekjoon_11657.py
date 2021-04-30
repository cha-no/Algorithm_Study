
'''

백준 문제

https://www.acmicpc.net/problem/11657

'''


n, m = list(map(int, input().split()))

flag = False
INF = 5000000000 + 1
distance = [0] + [INF] * (n - 1)

graph = [[] for i in range(n)]

for i in range(m):
    v1, v2, time = list(map(int, input().split()))
    graph[v1 - 1].append((v2 - 1, time))


for i in range(n):
    for v1 in range(n):
        for (v2, time) in graph[v1]:
            if distance[v1] != INF and distance[v2] > distance[v1] + time:
                distance[v2] = distance[v1] + time
                if i == n - 1:
                    flag = True

if flag:
    print(-1)
else:
    for dist in distance[1:]:
        print(-1 if dist == INF else dist)
