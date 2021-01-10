'''

hackerrank 문제

난이도 : hard

https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

'''

def maxRegion(grid):
    n = len(grid); m = len(grid[0])
    answer = -1
    visit = [[0]*m for i in range(n)]
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    stack = []
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                temp = 1
                x, y = i, j
                visit[x][y] = 1
                stack.append((x,y))
                while stack:
                    x, y = stack.pop()
                    for k in range(8):
                        if x+dx[k]<0 or x+dx[k]>=n or y+dy[k]<0 or y+dy[k]>=m:
                            continue
                        if grid[x+dx[k]][y+dy[k]] and not visit[x+dx[k]][y+dy[k]]:
                            temp += 1
                            visit[x+dx[k]][y+dy[k]] = 1
                            stack.append((x+dx[k],y+dy[k]))
                answer = max(answer,temp)
    return answer
