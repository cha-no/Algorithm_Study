
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12927?language=python3

'''

import heapq

def solution(n, works):
    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))

    for i in range(n):
        _, work = heapq.heappop(heap)
        if not work:
            break
        heapq.heappush(heap, (1 - work, work - 1))
    
    return sum(map(lambda x: x**2, list(zip(*heap))[1]))
