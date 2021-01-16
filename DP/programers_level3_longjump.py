
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12914?language=python3

'''

def solution(n):
    if n==1:
        return 1
    if n==2:
        return 2
    
    a, b = 2, 1
    for i in range(n-2):
        a, b = a+b, a
    
    return a % 1234567
