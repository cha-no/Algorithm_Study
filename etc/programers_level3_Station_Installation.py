
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12979?language=python3#

'''

import math

def solution(n, stations, w):
    answer = 0
    s = 0
    for station in stations:
        res = station - w - s - 1
        s = station + w
        if res > 0:
            answer += math.ceil(res / (2*w + 1))
    
    if s < n:
        res = n - s
        if res > 0:
            answer += math.ceil(res / (2*w + 1))
    
    return answer
