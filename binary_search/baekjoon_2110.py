
'''

백준 문제

https://www.acmicpc.net/problem/2110

'''

import sys

n, c = list(map(int, sys.stdin.readline().split()))
houses = sorted([int(sys.stdin.readline()) for i in range(n)])

s, e = 1, 1000000000
answer = 0

while s <= e:
    m = (s + e) // 2
    count = 0
    temp = houses[0]
    
    for i in range(1, n):
        if houses[i] - temp >= m:
            count += 1
            temp = houses[i]
    if count + 1 >= c:
        answer = m
        s = m + 1
    else:
        e = m - 1

print(answer)
