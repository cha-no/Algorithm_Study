
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/49995?language=python3

'''

from typing import List

def solution(cookie : List[int]) -> int:
    if len(cookie) == 1:
        return 0
    answer = -1
    sum_list = [0]
    for c in cookie:
        sum_list.append(sum_list[-1] + c)

    for s in range(len(sum_list) - 2):
        m = s + 1
        e = m + 1
        while s <= m and m <= e:
            if sum_list[e] - sum_list[m] == sum_list[m] - sum_list[s]:
                answer = max(answer, sum_list[e] - sum_list[m])
                e += 1
            elif sum_list[e] - sum_list[m] < sum_list[m] - sum_list[s]:
                e += 1
            else:
                m += 1
            if e > len(cookie):
                break
    
    return answer if answer > 0 else 0
