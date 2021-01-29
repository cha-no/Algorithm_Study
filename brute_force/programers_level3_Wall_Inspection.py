
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3#

'''

from itertools import permutations

def solution(n, weak, dist):
    def isPossible(weak_circle, friends, m = len(weak)):
        if m == 1:
            return True
        for i in range(m):
            cur = i
            prev = i
            check = 1
            for friend in friends:
                if check >= m:
                    return True
                while weak_circle[cur + 1] - weak_circle[prev] <= friend:
                    cur += 1
                    check += 1
                    if check >= m:
                        return True
                cur += 1
                prev = cur
                check += 1
        return False
    answer = -1
    count = 0
    weak_circle = []
    
    for w in weak:
        weak_circle.append(w)
    for w in weak:
        weak_circle.append(w + n)
    
    for i in range(1, len(dist) + 1):
        for friends in permutations(dist, i):
            if isPossible(weak_circle, friends):
                answer = i
                return answer
    return answer
