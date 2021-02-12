'''

백준 문제

https://www.acmicpc.net/problem/1967

'''

def find_distance(vertex : int, n : int) -> tuple([int, int]):
    stack = []
    visit = [0] * n
    dist = [0] * n
    visit[vertex] = 1
    stack = [vertex]
    
    m = 0
    m_v = 0
    while stack:
        u = stack.pop()
        for w, d in graph[u]:
            if visit[w]:
                continue

            visit[w] = 1
            dist[w] = dist[u] + d
            if m < dist[w]:
                m = dist[w]
                m_v = w
                
            stack.append(w)
    
    return m_v, m

if __name__ == "__main__":
    n = int(input())

    graph = [[] for i in range(n)]

    for i in range(n - 1):
        edge = list(map(int, input().split()))
        graph[edge[0] - 1].append((edge[1] - 1, edge[2]))
        graph[edge[1] - 1].append((edge[0] - 1, edge[2]))

    m_v, m = find_distance(0, n)
    m_v, m = find_distance(m_v, n)
    print(m)
