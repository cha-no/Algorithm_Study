
'''

백준 문제

https://www.acmicpc.net/problem/1956

'''


INF = 400 ** 2 * 10000 + 1

v, e = map(int, input().split())
distance = [[INF] * v for i in range(v)]

for i in range(e):
    a, b, c = map(int, input().split())
    distance[a - 1][b - 1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

answer = min([distance[i][i] for i in range(v)])
print(-1) if answer == INF else print(answer)
