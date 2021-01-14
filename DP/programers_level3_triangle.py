
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

'''

def solution(triangle):
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]
        for j in range(1, i):
            triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
    return max(triangle[-1])
