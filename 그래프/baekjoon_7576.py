'''

백준 문제

https://www.acmicpc.net/problem/7576

'''

import sys
from collections import deque

m, n = list(map(int, sys.stdin.readline().split()))
visit = []
queue = deque([])

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if temp[j]==1:
            queue.append((i,j))
    visit.append(temp)

answer = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        if x+dx[i]<0 or x+dx[i]>=n or y+dy[i]<0 or y+dy[i]>=m or visit[x+dx[i]][y+dy[i]]==-1:
            continue
        if not visit[x+dx[i]][y+dy[i]]:
            visit[x+dx[i]][y+dy[i]] = visit[x][y] + 1
            queue.append((x+dx[i], y+dy[i]))

flag = False
for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            flag = True
            answer = 0
            break
        answer = max(answer, visit[i][j])
    if flag:
        break
print(answer-1)
