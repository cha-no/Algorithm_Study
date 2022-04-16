
'''

백준 문제

https://www.acmicpc.net/problem/17472

'''


from typing import Tuple, List

class Island(object):
    def __init__(self, island_id: int, vertices: List[Tuple[int]]) -> None:
        self.__island_id = island_id
        self.__vertices = vertices

    @property
    def island_id(self) -> int:
        return self.__island_id
    
    @property
    def vertices(self) -> List[Tuple[int]]:
        return self.__vertices

def is_possible(x: int, y: int, n: int, m: int) -> bool:
    return 0 <= x < n and 0 <= y < m

def get_island(graph: List[List[int]], n: int, m: int) -> List[Island]:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[False] * m for i in range(n)]
    islands = []
    island_id = 0

    for i in range(n):
        for j in range(m):
            if visit[i][j]: continue        
            if graph[i][j]:
                stack = [(i, j)]
                vertices = []
                while stack:
                    x, y = stack.pop()
                    if visit[x][y]: continue

                    visit[x][y] = True
                    vertices.append((x, y))
                    for k in range(4):
                        new_x, new_y = x + dx[k], y + dy[k]
                        if is_possible(new_x, new_y, n, m) and not visit[new_x][new_y] and graph[new_x][new_y]:
                            stack.append((new_x, new_y))

                island = Island(island_id, vertices)
                islands.append(island)
                island_id += 1
            else: visit[i][j] = True
    return islands

def get_cost(v1: Tuple[int], v2: Tuple[int], id1: int, id2: int) -> int:
    x1, y1 = v1
    x2, y2 = v2
    
    flag = False
    if x1 == x2:
        for island in islands:
            for v in island.vertices:
                x, y = v
                if x == x1 and (abs(y2 - y) < abs(y2 - y1) and abs(y1 - y) < abs(y2 - y1)):
                    flag = True
                    break
            if flag: 
                cost = 0
                break
        else:
            cost = abs(y2 - y1)
    elif y1 == y2:
        for island in islands:
            for v in island.vertices:
                x, y = v
                if y == y1 and (abs(x2 - x) < abs(x2 - x1) and abs(x1 - x) < abs(x2 - x1)):
                    flag = True
                    break
            if flag: 
                cost = 0
                break
        else:
            cost = abs(x2 - x1)
    else:
        cost = 0
    return cost if cost > 2 else 0
    
def get_edge(island1: Island, island2: Island) -> int:
    vertices1, vertices2 = island1.vertices, island2.vertices
    id1, id2 = island1.island_id, island2.island_id
    
    edge = 0
    for v1 in vertices1:
        for v2 in vertices2:
            cost = get_cost(v1, v2, id1, id2)
            if cost and edge:
                edge = min(edge, cost)
            elif not cost: continue
            else:
                edge = cost
    return edge - 1

def find(v: int) -> int:
    return v if par[v] < 0 else find(par[v])

def is_connect(par: List[int]) -> bool:
    check = set()
    for v in range(len(par)): check.add(find(v))
    return True if len(check) == 1 else False

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for i in range(n)]
    
    islands = get_island(graph, n, m)
    num_of_islands = len(islands)

    edges = []
    for i in range(1, len(islands)):
        for j in range(i):
            cost = get_edge(islands[i], islands[j])
            if cost > 1:
                edges.append((i, j, cost))

    edges = sorted(edges, key=lambda x: x[2])
    par = [-1] * num_of_islands

    answer = 0
    for edge in edges:
        u, v, cost = edge
        if find(u) != find(v):
            if par[find(u)] < par[find(v)]:
                par[find(u)] += par[find(v)]
                par[find(v)] = find(u)
            else:
                par[find(v)] += par[find(u)]
                par[find(u)] = find(v)
            answer += cost

    if is_connect(par): print(answer)
    else: print(-1)
