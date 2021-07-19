
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/62050?language=python3

'''



from typing import List
from collections import deque
import heapq

def isPossible(x : int, y : int, n : int) -> bool:
    return 0 <= x < n and 0 <= y < n

def solution(land : List[int], height : int) -> int:
    answer = 0
    n = len(land)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[False] * n for i in range(n)]
    cur_visit = 0
    queue = deque([(0, 0)])
    heap = []
    
    while cur_visit < n ** 2:
        while queue:
            x, y = queue.popleft()
            
            if visit[x][y]:
                continue
            visit[x][y] = True
            cur_visit += 1
            
            for i in range(4):
                if not isPossible(x + dx[i], y + dy[i], n):
                    continue
                
                diff_height = abs(land[x][y] - land[x+dx[i]][y + dy[i]])
                
                if diff_height <= height:
                    queue.append((x+dx[i], y+dy[i]))
                else:
                    heapq.heappush(heap, (diff_height, x+dx[i], y+dy[i]))
        
        while heap:
            diff_height, x, y = heapq.heappop(heap)
            
            if visit[x][y]:
                continue
            answer += diff_height
            queue.append((x, y))
            break
        
    return answer
