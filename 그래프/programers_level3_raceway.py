
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3

'''



def solution(board):
    MAX = 25*25*600+1
    n = len(board)
    cost = [[MAX]*n for i in range(n)]
    cost[0][0] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    stack = [(0,0,0,-1)]
    
    while stack:
        x, y, c, d = stack.pop()
        for i in range(4):
            if x+dx[i]<0 or x+dx[i]>=n or y+dy[i]<0 or y+dy[i]>=n or board[x+dx[i]][y+dy[i]]:
                continue
            bonus = 0
            if d!=i and d!=-1:
                bonus += 500
            if cost[x+dx[i]][y+dy[i]] >= c+100+bonus:
                cost[x+dx[i]][y+dy[i]] = c+100+bonus
                stack.append((x+dx[i], y+dy[i], c+100+bonus, i))
    
    return cost[-1][-1]
