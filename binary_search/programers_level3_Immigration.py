
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3#

'''

def solution(n, times):
    answer = 10**15+1
    s, e = 1, 10**15+1
    
    while s<=e:
        m = (s+e)//2
        p = 0
        for time in times:
            p += m//time
        if p >= n:
            e = m-1
            answer = min(answer,m)
        else:
            s = m+1
        
    return answer
