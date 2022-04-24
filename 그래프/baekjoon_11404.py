
'''

백준 문제

https://www.acmicpc.net/problem/11404

'''


INF = 100000 * 100 + 1

n, m = int(input()), int(input())
distance = [[INF] * n for i in range(n)]

for i in range(n):
    distance[i][i] = 0

for i in range(m):
    u, v, cost = map(int, input().split())
    distance[u - 1][v - 1] = min(distance[u - 1][v - 1], cost)

for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for dd in distance:
    answer = [0 if d == INF else d for d in dd]
    print(" ".join(map(str, answer)))
