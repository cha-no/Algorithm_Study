
'''

백준 문제

https://www.acmicpc.net/problem/2667

'''

n = int(input())

graph = [list(map(int, list(input()))) for _ in range(n)]

house = []
visit = [[0] * n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if visit[i][j]:
            continue
        if graph[i][j]:
            temp = 0
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if visit[x][y]:
                    continue
                
                visit[x][y] = 1
                temp += 1
                for k in range(4):
                    if x + dx[k] < 0 or x + dx[k] >= n or y + dy[k] < 0 or y + dy[k] >= n or visit[x + dx[k]][y + dy[k]]:
                        continue
                    if graph[x + dx[k]][y + dy[k]]:
                        stack.append((x + dx[k], y + dy[k]))
            house.append(temp)

print(len(house))
house.sort()
for h in house:
    print(h)
