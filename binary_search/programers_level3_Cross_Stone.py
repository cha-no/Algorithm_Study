
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/64062?language=python3#

'''

def solution(stones, k):
    def isPossible(stones, k, n):
        p = 0
        for stone in stones:
            if stone < n:
                p += 1
            else:
                if p >= k:
                    return False
                p = 0
        if p >= k:
            return False
        return True
    
    answer = 0
    s, e = 1, 200000000 + 1
    
    while s <= e:
        m = (s + e) // 2
        if isPossible(stones, k, m):
            answer = max(answer, m)
            s = m + 1
        else:
            e = m - 1
        
    return answer
