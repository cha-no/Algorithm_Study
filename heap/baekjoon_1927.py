'''

백준 문제

https://www.acmicpc.net/problem/1927

'''

import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    info = int(sys.stdin.readline())
    heapq.heappush(heap, info) if info else print(heapq.heappop(heap)) if heap else print(0)
