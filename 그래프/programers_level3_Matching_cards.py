
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/72415?language=python3#

'''

from typing import List, Tuple, Dict
from itertools import permutations
from copy import deepcopy

def solution(board : List[List[int]], r : int, c : int) -> int:
    def xCost(board : List[List[int]], r : int, c : int, t_r : int) -> int:
        x_cost = 1
        if r == t_r:
            return 0
        elif r > t_r:
            for i in range(r - 1, t_r, -1):
                if board[i][c]:
                    x_cost += 1
            
            if x_cost == 1 and r == 3 and t_r == 1 and not board[t_r][c]:
                x_cost += 1
            
        else:
            for i in range(r + 1, t_r):
                if board[i][c]:
                    x_cost += 1
            
            if x_cost == 1 and r == 0 and t_r == 2 and not board[t_r][c]:
                x_cost += 1
            
        return x_cost
    def yCost(board : List[List[int]], r : int, c : int, t_c : int) -> int:
        y_cost = 1
        if c == t_c:
            return 0
        elif c > t_c:
            for j in range(c - 1, t_c, -1):
                if board[r][j]:
                    y_cost += 1
            
            if y_cost == 1 and c == 3 and t_c == 1 and not board[r][t_c]:
                y_cost += 1
            
        else:
            for j in range(c + 1, t_c):
                if board[r][j]:
                    y_cost += 1
            
            if y_cost == 1 and c == 0 and t_c == 2 and not board[r][t_c]:
                y_cost += 1
            
        return y_cost
    def getCost(board : List[List[int]], r : int, c : int, t_r : int, t_c : int) -> int:
        if r == t_r and c == t_c:
            return 0, [r, c]
        cost = 9876543210
        if t_r == r:
            cost = yCost(board, r, c, t_c)
        elif t_c == c:
            cost = xCost(board, r, c, t_r)
        else:
            for i in range(min(r, t_r), max(r, t_r) + 1):
                cost = min(cost, xCost(board, r, c, i) + yCost(board, i, c, t_c) + xCost(board, i, t_c, t_r))
            for j in range(min(c, t_c), max(c, t_c) + 1):
                cost = min(cost, yCost(board, r, c, j) + xCost(board, r, j, t_r) + yCost(board, t_r, j, t_c))

        return cost, [t_r, t_c]
    def cost(board : List[List[int]], r : int, c : int, iters : Tuple[int], posses : Dict[int, List], poss_num : int) -> int:
        m_cost = 9876543210
        for i in range(2 ** poss_num):
            for j in range(poss_num):
                if not i % (2 ** j):
                    posses[poss_num - j].reverse()
                
            board_copy = deepcopy(board)
            s_r, s_c = r, c
            m = 0
            for k in iters:
                for (t_r, t_c) in posses[k]:
                    if s_r == t_r and s_c == t_c:
                        board_copy[s_r][s_c] = 0
                        m += 1
                        continue
                    temp, (s_r, s_c) = getCost(board_copy, s_r, s_c, t_r, t_c)
                    board_copy[s_r][s_c] = 0
                    m += temp + 1
            m_cost = min(m_cost, m)
        return m_cost
    answer = 9876543210
    posses = {}
    poss_num = 0
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]:
                posses[board[i][j]] = posses.get(board[i][j], [])
                posses[board[i][j]].append((i, j))
                poss_num += 1
    poss_num //= 2
    
    for iters in permutations(range(1, poss_num + 1), poss_num):
        answer = min(answer, cost(board, r, c, iters, posses, poss_num))
    
    return answer
