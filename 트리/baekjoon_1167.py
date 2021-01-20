'''

백준 문제

https://www.acmicpc.net/problem/1167

'''
def find_distance(vertex):
    stack = []
    visit = [0]*v
    dist = [0]*v
    visit[vertex] = 1
    stack = [vertex]
    
    m = 0
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
    v = int(input())

    graph = [[] for i in range(v)]

    for i in range(v):
        edge = list(map(int, input().split()))
        for j in range(1,len(edge)-1,2):
            graph[edge[0]-1].append((edge[j]-1, edge[j+1]))

    m_v, m = find_distance(0)
    m_v, m = find_distance(m_v)
    print(m)
