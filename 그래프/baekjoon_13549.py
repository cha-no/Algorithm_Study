
'''

백준 문제

https://www.acmicpc.net/problem/13549

'''

import heapq

INF = 100000 + 1

def is_valid(v: int) -> bool:
    return 0 <= v <= 100000

if __name__ == "__main__":
    n, k = map(int, input().split())
    
    distance = [INF] * INF
    distance[n] = 0
    visit = [False] * INF

    heap = [(0, n)]

    while heap:
        cost, u = heapq.heappop(heap)

        if visit[u]: continue
        visit[u] = True

        v = 2 * u
        while v < 100001:
            if not v: break
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(heap, (cost, v))
            v *= 2
        if is_valid(u + 1) and cost + 1 < distance[u + 1]:
            distance[u + 1] = cost + 1
            heapq.heappush(heap, (cost + 1, u + 1))
        if is_valid(u - 1) and cost + 1 < distance[u - 1]:
            distance[u - 1] = cost + 1
            heapq.heappush(heap, (cost + 1, u - 1))
    
    print(distance[k])
