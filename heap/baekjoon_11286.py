'''

백준 문제

https://www.acmicpc.net/problem/11286

'''

import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    heap = []
    
    for i in range(n):
        oper = int(sys.stdin.readline())
        if oper:
            heapq.heappush(heap, (abs(oper), oper))
        else:
            if heap:
                key, item = heapq.heappop(heap)
                print(item)
            else:
                print(0)
