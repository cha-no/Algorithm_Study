'''

백준 문제

https://www.acmicpc.net/problem/5430

'''

from collections import deque

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    integers = input().lstrip('[').rstrip(']')
    arr = deque(list(map(int, integers.split(','))) if integers else [])

    s = 0
    flag = True
    for f in p:
        if f=='D':
            if arr:
                arr.pop() if s else arr.popleft()
            else:
                print('error')
                flag = False
                break
        else:
            s^=1
    if not flag:
        continue
    if s:
        arr.reverse()

    print(str(list(arr)).replace(' ',''))
