
'''

백준 문제

https://www.acmicpc.net/problem/4803

'''

from typing import List

def dfs(v: int, vertices: List[int]) -> None:
    vertex_visit[v] = True
    vertices.append(v)

    for edge in vertex_to_edge[v]:
        if edge_visit[edge]: continue
        u, w = edges[edge]
        if not(vertex_visit[u] and vertex_visit[w]):
            edge_visit[edge] = True
            if u == v:
                dfs(w, vertices)
            elif w == v:
                dfs(u, vertices)
            else:
                raise Exception("error")

if __name__ == "__main__":
    case = 0
    while True:
        n, m = map(int, input().split())
        if not (n or m): break
        case += 1
        edges = []
        vertex_to_edge = [[] for i in range(n)]
        vertex_visit = [False] * n
        edge_visit = [False] * m

        for i in range(m):
            u, v = map(int, input().split())
            edges.append([u - 1, v - 1])
            vertex_to_edge[u - 1].append(i)
            vertex_to_edge[v - 1].append(i)

        components = 0
        trees = 0
        for u in range(n):
            if not vertex_visit[u]:
                components += 1
                vertices = []
                dfs(u, vertices)

                tree_flag = True
                for vertex in vertices:
                    for edge in vertex_to_edge[vertex]:
                        if not edge_visit[edge]:
                            tree_flag = False
                            break
                    if not tree_flag: break
                if tree_flag: trees += 1

        if trees > 1:
            print(f"Case {case}: A forest of {trees} trees.")
        elif trees == 1:
            print(f"Case {case}: There is one tree.")
        else:
            print(f"Case {case}: No trees.")
            
