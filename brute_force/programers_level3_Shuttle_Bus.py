
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/17678?language=python3

'''

from typing import List

def solution(n : int, t : int, m : int, timetable : List[str]) -> str:
    def convert(time : str) -> int:
        return int(time[:2]) * 60 + int(time[-2:])
    
    def inverseConvert(time : int) -> str:
        hour, minute = str(time // 60), str(time % 60)
        if len(hour) == 1:
            hour = '0' + hour
        if len(minute) == 1:
            minute = '0' + minute
        return hour + ':' + minute
    
    cur = convert('09:00')
    timetable = sorted(timetable)
    index = 0
    p = 0
    
    for i in range(n):
        k = 0
        for j in range(m):
            if index < len(timetable) and convert(timetable[index]) <= cur:
                index += 1
                k += 1
            else: break
        if index == len(timetable) or i == n - 1:
            p = k
            break
        cur += t

    return inverseConvert(convert(timetable[index - 1]) - 1) if m == p else inverseConvert(cur)
