
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/68646?language=python3#

'''

def solution(a):
    answer = 0
    left_min = []
    right_min = []
    
    for num in a:
        if not left_min:
            left_min.append(num)
        else:
            if left_min[-1] > num:
                left_min.append(num)
    
    while a:
        num = a.pop()
        if not right_min:
            right_min.append(num)
            answer += 1
        else:
            if num <= left_min[-1] or num <= right_min[-1]:
                answer += 1
                right_min.append(num)
        
        if num == left_min[-1]:
            left_min.pop()
    
    return answer
