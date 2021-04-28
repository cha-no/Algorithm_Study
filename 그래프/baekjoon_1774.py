
'''

백준 문제

https://www.acmicpc.net/problem/1774

'''

import sys
from typing import List

sys.setrecursionlimit(20000)

def get_distance(vertex1 : List[int], vertex2 : List[int]) -> float:
    x1, y1 = vertex1
    x2, y2 = vertex2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def find(index : int) -> int:
    return index if par[index] < 0 else find(par[index])


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    vertices = [list(map(int, input().split())) for i in range(n)]

    answer = 0
    par = [-1] * n
    edges = []

    for i in range(m):
        v1, v2 = list(map(int, input().split()))
        if find(v1 - 1) != find(v2 - 1):
            if par[find(v1 - 1)] <= par[find(v2 - 1)]:
                par[find(v1 - 1)] += par[find(v2 - 1)]
                par[find(v2 - 1)] = find(v1 - 1)
            else:
                par[find(v2 - 1)] += par[find(v1 - 1)]
                par[find(v1 - 1)] = find(v2 - 1)
    
    for i in range(n):
        for j in range(n):
            if i <= j:
                continue
            edges.append((i, j, get_distance(vertices[i], vertices[j])))

    edges = sorted(edges, key = lambda x : x[2])

    for edge in edges:
        v1, v2, cost = edge
        if find(v1) != find(v2):
            answer += cost
            m += 1
            if m == n - 1:
                break
            if par[find(v1)] <= par[find(v2)]:
                par[find(v1)] += par[find(v2)]
                par[find(v2)] = find(v1)
            else:
                par[find(v2)] += par[find(v1)]
                par[find(v1)] = find(v2)

    print(f"{answer:.2f}")
