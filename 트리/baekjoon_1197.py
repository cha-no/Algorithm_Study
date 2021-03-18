'''

백준 문제

https://www.acmicpc.net/problem/1197

'''
# prim algorithm

import heapq

v, e = list(map(int, input().split()))

graph = [[] for _ in range(v)]

for _ in range(e):
    v1, v2, cost = list(map(int, input().split()))
    graph[v1- 1].append((v2, cost))
    graph[v2- 1].append((v1, cost))
    
answer = 0
heap = [(0, 1)]
visit = [0] * v

while heap:
    cost, u = heapq.heappop(heap)
    if visit[u - 1]:
        continue
    
    answer += cost
    visit[u - 1] = 1
    for (w, c) in graph[u - 1]:
        if visit[w - 1]:
            continue
        heapq.heappush(heap, (c, w))

print(answer)



# kruskal algorithm

def find(v):
    return v if par[v]<0 else find(par[v])

if __name__== "__main__":
    answer = 0
    v, e = list(map(int, input().split()))
    par = [-1]*v
    edges = []
    for i in range(e):
        edges.append(list(map(int, input().split())))
    edges = sorted(edges, key = lambda x:x[2])

    for edge in edges:
        if find(edge[0]-1) != find(edge[1]-1):
            answer += edge[2]
            if par[find(edge[0]-1)] <= par[find(edge[1]-1)]:
                par[find(edge[0]-1)] += par[find(edge[1]-1)]
                par[find(edge[1]-1)] = find(edge[0]-1)
            else:
                par[find(edge[1]-1)] += par[find(edge[0]-1)]
                par[find(edge[0]-1)] = find(edge[1]-1)   
    print(answer)
