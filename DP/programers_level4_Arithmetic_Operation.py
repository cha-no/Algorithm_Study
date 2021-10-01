
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/1843?language=python3

'''


from typing import List

def solution(arr : List[str]) -> int:
    dp_min, dp_max = 0, 0
    temp_sum = 0
    for i in range(len(arr)-1, 0, -2) :
        oper, num = arr[i-1], int(arr[i])
        if oper == "-" :
            dp_min, dp_max = min(-num - temp_sum + dp_min, -(num + temp_sum + dp_max)), max(-(num + temp_sum + dp_min), -num + temp_sum + dp_max)
            temp_sum = 0
        else : temp_sum += num
        
    return dp_max + temp_sum + int(arr[0])
