
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/77886?language=python3#

'''


STR = '110'
from typing import List

def is_exist(stack : List[str]) -> bool:
    return True if len(stack) >= 3 and stack[-3:] == ['1', '1', '0'] else False

def find_index(s : str) -> int:
    index = s.find('11')
    if index == -1:
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                index = i + 1
                break
    return index

def solution(s : List[str]) -> List[str]:
    answer = []
    for string in s:
        count = 0
        stack = []
        for char in string:
            stack.append(char)

            while is_exist(stack):
                count += 1
                for i in range(3):
                    stack.pop()
        string = ''.join(stack)

        if not string or (len(string) == 1 and string.startswith('1')):
            string = STR * count + string
        elif find_index(string) >= 0:
            index = find_index(string)
            string = string[:index] + STR * count + string[index:]
        answer.append(string)

    return answer
