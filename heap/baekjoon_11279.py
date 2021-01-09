'''

백준 문제

https://www.acmicpc.net/problem/11279

'''

import sys
import heapq

n = int(sys.stdin.readline())
heap = []
size = 0

for i in range(n):
    item = int(sys.stdin.readline())
    if not item:
        if size:
            print(heapq.heappop(heap)[1])
            size -= 1
        else:
            print(0)
    else:
        heapq.heappush(heap,(-item,item))
        size += 1
