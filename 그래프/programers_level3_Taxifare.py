
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/72413?language=python3

'''
import heapq
INF = 100000 * 200 + 1

def solution(n, s, a, b, fares):
    def getCost(cur, dest):
        visit = [0] * n
        distance = [INF] * n
        distance[cur - 1] = 0
        heap = [(0, cur)]
        
        while heap:
            dist, cur = heapq.heappop(heap)
            if visit[cur - 1]:
                continue

            visit[cur - 1] = 1

            for (point, cost) in graph[cur - 1]:
                if distance[point - 1] > distance[cur - 1] + cost:
                    distance[point - 1] = distance[cur - 1] + cost
                    heapq.heappush(heap, (distance[point - 1], point))
                    
        return distance[dest - 1]
    
    answer = INF
    graph = [[] for i in range(n)]
    
    for fare in fares:
        graph[fare[0] - 1].append((fare[1], fare[2]))
        graph[fare[1] - 1].append((fare[0], fare[2]))
    
    visit = [0] * n
    heap = [(0, s)]
    visit[s - 1] = 1
    
    while heap:
        dist, cur = heapq.heappop(heap)
        visit[cur - 1] = 1
        if answer <= dist:
            continue
        dist_a = getCost(cur, a)
        dist_b = getCost(cur, b)
        if answer > dist_a + dist_b + dist:
            answer = dist_a + dist_b + dist

        for (point, cost) in graph[cur - 1]:
            if visit[point - 1]:
                continue
            heapq.heappush(heap, (dist + cost, point))
    
    return answer
