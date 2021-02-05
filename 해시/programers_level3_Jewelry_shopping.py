
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3#

'''

def solution(gems):
    answer = [1, len(gems)]
    total = len(set(gems))
    cur_gems = {}
    s, e = 0, 0
    while s <= e:
        if len(cur_gems) == total:
            if cur_gems[gems[s]] == 1:
                if e - s - 1 < answer[1] - answer[0]:
                    answer = [s + 1, e]
                cur_gems.pop(gems[s])
            else:
                cur_gems[gems[s]] -= 1
            s += 1
        elif e < len(gems):
            cur_gems[gems[e]] = cur_gems.get(gems[e], 0) + 1
            e += 1
        else:
            s += 1
    
    return answer
