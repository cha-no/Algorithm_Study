
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/84021?language=python3

'''


from typing import List, Set, Tuple
from collections import deque

def isPossible(x:int, y:int, board:List[List[int]]) -> bool:
    return 0 <= x < len(board) and 0 <= y < len(board)

def bfs(r:int, c:int, board:List[List[int]], find_zero:bool=True) -> Set[Tuple[int]]:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    block_set = set()
    queue = deque([(r, c)])
    while queue:
        x, y = queue.popleft()
        if (x-r, y-c) in block_set:
            continue
        
        block_set.add((x-r, y-c))
        
        for i in range(4):
            if isPossible(x+dx[i], y+dy[i], board):
                if find_zero and not board[x+dx[i]][y+dy[i]]:
                    queue.append((x+dx[i], y+dy[i]))
                elif not find_zero and board[x+dx[i]][y+dy[i]] == 1:
                    queue.append((x+dx[i], y+dy[i]))
    return block_set

def rotate(block_set:Set[int]) -> Set[int]:
    max_n, min_n = max([max(xy) for xy in block_set]), min([min(xy) for xy in block_set])
    n = max_n - min_n
    board = [[0]*(n+1) for _ in range(n+1)]
    rotate_board = [[0]*(n+1) for _ in range(n+1)]

    for x, y in block_set:
        board[x-min_n][y-min_n] = 1

    for i in range(n+1):
        for j in range(n+1):
            if board[i][j]:
                rotate_board[n-j][i] = 1

    for i in range(n+1):
        for j in range(n+1):
            if rotate_board[i][j]:
                return bfs(i, j, rotate_board, False)

def checkSame(board_block_set:Set[int], table_block_set:Set[int]) -> bool:
    return board_block_set == table_block_set

def solution(game_board:List[List[int]], table:List[List[int]]) -> int:
    answer = 0
    board_block_set_list = []
    table_block_set_list = []
    
    visit = [[0]*len(game_board) for _ in range(len(game_board))]
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if not (game_board[i][j] or visit[i][j]):
                block_set = bfs(i, j, game_board, True)
                board_block_set_list.append(block_set)
                for (x, y) in block_set:
                    visit[x+i][y+j] = 1

    visit = [[0]*len(game_board) for _ in range(len(game_board))]
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if table[i][j] and not visit[i][j]:
                block_set = bfs(i, j, table, False)
                table_block_set_list.append(block_set)
                for (x, y) in block_set:
                    visit[x+i][y+j] = 1
    
    checklist = [False] * len(board_block_set_list)
    for table_block_set in table_block_set_list:
        flag = False
        for (i, board_block_set) in enumerate(board_block_set_list):
            for j in range(4):
                if (checkSame(board_block_set, table_block_set) and not checklist[i]):
                    answer += len(board_block_set)
                    checklist[i] = True
                    flag = True
                board_block_set = rotate(board_block_set)
            if flag:
                break

    return answer
