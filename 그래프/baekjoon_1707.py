
'''

백준 문제

https://www.acmicpc.net/problem/1707

'''

from collections import deque

def bfs(v: int, e: int) -> str:
    graph = [[] for i in range(v)]

    for i in range(e):
        u, w = map(int, input().split())
        graph[u - 1].append(w - 1)
        graph[w - 1].append(u - 1)

    visit = [False] * v
    color = [0] * v

    for u in range(v):
        if visit[u]: continue
        color[u] = 1
        queue = deque([u])

        while queue:
            w = queue.popleft()

            if visit[w]: continue
            visit[w] = True

            for x in graph[w]:
                if visit[x]:
                    if color[x] == color[w]: return 'NO'
                else:
                    if color[w] == 1:
                        color[x] = 2
                    else:
                        color[x] = 1
                    queue.append(x)
    return 'YES'

if __name__ == "__main__":
    k = int(input())
    for i in range(k):
        v, e = map(int, input().split())
        print(bfs(v, e))
