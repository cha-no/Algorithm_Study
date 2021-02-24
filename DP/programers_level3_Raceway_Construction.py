
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3

'''

from typing import List

def solution(board : List[List[int]]) -> int:
    INF = 25 ** 2 * 600 + 1
    answer = INF
    n = len(board)
    raceway = [[INF] * n for i in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    raceway[0][0] = 0
    queue = [(0, 0, 0, -1)]
    
    while queue:
        (x, y, cost, d), queue = queue[0], queue[1:]
        if x == n - 1 and y == n - 1:
            answer = min(answer, cost)
        
        for i in range(4):
            if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= n or board[x + dx[i]][y + dy[i]]:
                continue
            
            corner = 0            
            if d >= 0 and d != i:
                corner += 500
            
            if raceway[x + dx[i]][y + dy[i]] >= cost + 100 + corner:
                raceway[x + dx[i]][y + dy[i]] = cost + 100 + corner
                queue.append((x + dx[i], y + dy[i], cost + 100 + corner, i))
            
    return answer
