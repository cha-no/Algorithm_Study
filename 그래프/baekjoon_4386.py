'''

백준 문제

https://www.acmicpc.net/problem/4386

'''

def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

if __name__ == "__main__":
    n = int(input())

    coords = []

    for i in range(n):
        coords.append(list(map(float, input().split())))

    INF = 1500
    graph = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            graph[i][j] = distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
            graph[j][i] = distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])

    visit = [0] * n
    cur = 0
    visit[cur] = 1
    distance = graph[cur]

    for i in range(n):
        m = INF
        index = 0
        for j in range(n):
            if visit[j] or cur == j:
                continue
            if graph[cur][j] < m:
                m = graph[cur][j]
                index = j

        visit[index] = 1
        for j in range(n):
            if visit[j]:
                continue
            if graph[index][j] < distance[j]:
                distance[j] = graph[index][j]
    print(round(sum(distance),2))
