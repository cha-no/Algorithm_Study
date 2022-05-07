
'''

백준 문제

https://www.acmicpc.net/problem/7569

'''


from collections import deque

def is_possible(x: int, y: int, z: int) -> bool:
    return 0 <= x < len(graph[0][0]) and 0 <= y < len(graph[0]) and 0 <= z < len(graph)

if __name__ == "__main__":
    m, n, h = map(int, input().split())
    graph = [[] for i in range(h)]
    queue = deque([])
    remains = 0

    for i in range(h):
        for j in range(n):
            graph[i].append(list(map(int, input().split())))
            for k in range(m):
                if graph[i][j][k] == 1: 
                    queue.append(((i, j, k), 0))
                    remains += 1
            remains += graph[i][j].count(0)

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    answer = -1
    days = 0
    visit = [[[False] * m for i in range(n)] for j in range(h)]

    while queue:
        (z, y, x), day = queue.popleft()
        if visit[z][y][x]: continue

        days = max(days, day)
        visit[z][y][x] = True
        graph[z][y][x] = 1
        remains -= 1

        for i in range(6):
            new_x, new_y, new_z = x + dx[i], y + dy[i], z + dz[i]
            if is_possible(new_x, new_y, new_z) and not graph[new_z][new_y][new_x]:
                queue.append(((new_z, new_y, new_x), day + 1))

    print(-1 if remains > 0 else days)
