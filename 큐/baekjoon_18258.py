
'''

백준 문제

https://www.acmicpc.net/problem/18258

'''

import sys
from collections import deque

queue = deque([])

n = int(sys.stdin.readline())
size = 0
for i in range(n):
    query = sys.stdin.readline().split()
    if query[0]=='push':
        queue.append(int(query[1]))
        size += 1
    elif query[0]=='pop':
        if size:
            print(queue.popleft())
            size -= 1
        else:
            print(-1)
    elif query[0]=='size':
        print(size)
    elif query[0]=='empty':
        if size:
            print(0)
        else:
            print(1)
    elif query[0]=='front':
        if size:
            print(queue[0])
        else:
            print(-1)
    else:
        if size:
            print(queue[-1])
        else:
            print(-1)
