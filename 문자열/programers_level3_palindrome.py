
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/12904?language=python3#

'''

def solution(s):
    def check(s):
        return True if s[:len(s)//2] == s[::-1][:len(s)//2] else False
    
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            if check(s[j:j+i]):
                return i

    return 1
