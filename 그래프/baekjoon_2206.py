
'''

백준 문제

https://www.acmicpc.net/problem/2206

'''

from collections import deque

n, m = map(int, input().split())
graph = [input() for i in range(n)]

answer = n * m + 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visit = [[0] * m for i in range(n)]
visit[0][0] = 2

queue = deque([(0, 0, 1, False)])
while queue:
    x, y, dist, flag = queue.popleft()
    if x == n - 1 and y == m - 1:
        answer = min(answer, dist)
        break

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if not (0 <= new_x < n and 0 <= new_y < m) or (visit[new_x][new_y] == 2): continue

        if visit[new_x][new_y]:
            if not flag:
                if graph[new_x][new_y] == '0':
                    queue.append((new_x, new_y, dist + 1, flag))
                elif graph[new_x][new_y] == '1':
                    queue.append((new_x, new_y, dist + 1, True))      
                visit[new_x][new_y] = 2  
        else:
            if flag:
                if graph[new_x][new_y] == '0':
                    visit[new_x][new_y] = 1
                    queue.append((new_x, new_y, dist + 1, flag))
            else:
                if graph[new_x][new_y] == '0':
                    queue.append((new_x, new_y, dist + 1, flag))
                elif graph[new_x][new_y] == '1':
                    queue.append((new_x, new_y, dist + 1, True))        
                visit[new_x][new_y] = 2

print(-1 if answer == n * m + 1 else answer)
