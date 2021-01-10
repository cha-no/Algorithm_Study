'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

'''

def minimumMoves(grid, startX, startY, goalX, goalY):
    answer = 0
    N = len(grid)
    visit = [[0]*N for i in range(N)] 
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    queue = [(startX, startY)]
    
    while queue:
        cur, queue = queue[0], queue[1:]
        x, y = cur
        temp_x, temp_y = x, y
        for i in range(4):
            count = 0
            x, y = temp_x, temp_y
            while True:
                move_x, move_y = x+dx[i], y+dy[i]
                if move_x >= N or move_y >= N or move_x < 0 or move_y < 0 or grid[move_x][move_y] == 'X':
                    if count:
                        if not visit[x][y] or visit[x][y] > visit[temp_x][temp_y] + 1:
                            visit[x][y] = visit[temp_x][temp_y] + 1
                            queue.append((x,y))
                    break
                x, y = move_x, move_y
                if not visit[x][y] or visit[x][y] > visit[temp_x][temp_y] + 1:
                    visit[x][y] = visit[temp_x][temp_y] + 1
                    queue.append((x,y))
                if not count:
                    count = 1
    return visit[goalX][goalY]
