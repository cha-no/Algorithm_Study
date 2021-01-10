
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12936?language=python3#

'''

def solution(n, k):
    def factorial(n):
        return n*factorial(n-1) if n else 1
    answer = []
    visit = [i for i in range(1, n+1)]

    for i in range(n,0,-1):
        n_fact = factorial(i-1)
        order = (k-1) // n_fact
        k -= n_fact*order
        answer.append(visit.pop(order))
    return answer
