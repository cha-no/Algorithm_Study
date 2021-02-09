
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3

'''

def solution(routes):
    answer = 0
    cur = -30000 - 1
    routes = sorted(routes, key = lambda x : x[1])
    
    for route in routes:
        if cur < route[0]:
            answer += 1
            cur = route[1]
    
    return answer
