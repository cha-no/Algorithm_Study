'''

백준 문제

https://www.acmicpc.net/problem/1655

'''


import sys
import heapq

n = int(sys.stdin.readline())
min_heap, max_heap = [], []
n1, n2 = 0, 0

for i in range(n):
    num = int(sys.stdin.readline())
    
    if n1 != n2:
        heapq.heappush(min_heap, num)
        n1 += 1
    else:
        heapq.heappush(max_heap, -num)
        n2 += 1
        
    if min_heap and min_heap[0] < -max_heap[0]:
        median1 = heapq.heappop(min_heap)
        median2 = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, median2)
        heapq.heappush(max_heap, -median1)
        
    print(-max_heap[0])
