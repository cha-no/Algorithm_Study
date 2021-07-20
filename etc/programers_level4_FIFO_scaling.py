
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/12920?language=python3#

'''


from typing import List

def solution(n : int, cores : List[int]) -> int:
    s, e = 1, 500000000
    time = e
    count = 0
    res = []
    
    while s <= e:
        flag = False
        m = (s + e) // 2
        c = 0
        for i in range(len(cores)):
            c += m // cores[i] + 1
            if c >= n:
                time = min(time, m)
                flag = True
                break
        if flag:
            e = m - 1
        else:
            s = m + 1

    for i, core in enumerate(cores):
        count += (time - 1) // core + 1
        r = (time // core + 1) * core - core if not time % core else (time // core + 1) * core
        res.append((i + 1, r))
        
    return sorted(res, key = lambda x : x[1])[n - count - 1][0]
