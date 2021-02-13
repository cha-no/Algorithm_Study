
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3#

'''

def solution(key : list, lock : list) -> bool:
    def rotate(key : list) -> list:
        n = len(key)
        rotate_key = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                rotate_key[j][-1 - i] = key[i][j]
        return rotate_key
    
    def isPossible(key : list, lock : list, r : int, c : int) -> bool:
        n = len(key)
        m = len(lock)
        for _ in range(4):
            poss = True
            for i in range(m):
                for j in range(m):
                    if (r <= i < r + n and c <= j < c + n):
                        if not lock[i][j]^key[i - r][j - c]:
                            poss = False
                            break
                    else:
                        if not lock[i][j]:
                            poss = False
                            break
            if poss:
                break
            key = rotate(key)
        return poss

    answer = False
    for i in range(-len(key) + 1, len(lock)):
        for j in range(-len(key) + 1, len(lock)):
            answer = isPossible(key, lock, i, j)
            if answer:
                return answer
    return answer
