
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12987?language=python3#

'''

def solution(A : list, B : list) -> int:
    A.sort(), B.sort()
    answer = 0
    
    while A:
        a = A.pop()
        if B and a < B[-1]:
            B.pop()
            answer += 1
    
    return answer
