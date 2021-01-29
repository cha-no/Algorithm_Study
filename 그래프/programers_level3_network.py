
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

'''

def solution(n, computers):
    answer = 0
    visit = [0] * n
    stack = []
    
    for i in range(n):
        if visit[i]:
            continue
        answer += 1
        visit[i] = answer
        stack = [i]
        
        while stack:
            j = stack.pop()
            for k in range(n):
                if j == k or visit[k] or not computers[j][k]:
                    continue
                visit[k] = answer
                stack.append(k)
    return answer
