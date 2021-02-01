
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12952?language=python3

'''

def solution(n):
    def promising(k):
        for i in range(k):
            if chess[i] == chess[k] or abs(chess[i] - chess[k]) == k - i:
                return False
        return True
    
    answer = 0
    chess = [0] * n
    s = 0
    while s >= 0:
        while chess[s] < n:
            chess[s] += 1
            if promising(s):
                if s < n - 1:
                    s += 1
                    chess[s] = 0
                else:
                    answer += 1
        s -= 1
    return answer
