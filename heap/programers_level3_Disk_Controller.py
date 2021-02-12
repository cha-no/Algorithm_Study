
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3#

'''

import heapq

def solution(jobs):
    jobs.sort()
    heap = []
    cur = 0
    total = 0
    n = 0
    
    for s, t in jobs:
        if not heap:
            cur = s
        while cur <= s and heap:
            time, start = heapq.heappop(heap)
            total += time + cur - start
            cur += time
        heapq.heappush(heap, [t, s])
        n += 1
    else:
        while heap:
            time, start = heapq.heappop(heap)
            total += time + cur - start
            cur += time
    
    return total // n
