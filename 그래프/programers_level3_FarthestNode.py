
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

'''

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n)]
    for e in edge:
        graph[e[0]-1].append(e[1]-1)
        graph[e[1]-1].append(e[0]-1)
    
    dist = [0]*n
    queue = [0]
    
    while queue:
        v, queue = queue[0], queue[1:]
        
        for u in graph[v]:
            if dist[u] or not u:
                continue
            
            dist[u] = dist[v] + 1
            queue.append(u)
    
    return dist.count(max(dist))
