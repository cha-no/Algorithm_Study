
'''
백준 문제

https://www.acmicpc.net/problem/2346

'''
    
from collections import deque

n = int(input())
explodes = list(map(int, input().split()))

queue = deque([i + 1 for i in range(n)])
queue

answer = []
for i in range(n):
    top = queue.popleft()
    answer.append(str(top))
    exp = -explodes[top - 1]
    exp = exp if exp > 0 else exp + 1
    queue.rotate(exp)

print(' '.join(answer))
