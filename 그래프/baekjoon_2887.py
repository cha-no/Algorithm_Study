
'''

백준 문제

https://www.acmicpc.net/problem/2887

'''

def find(v: int) -> int:
    return v if par[v] < 0 else find(par[v])

if __name__ == "__main__":
    n = int(input())
    coords = [list(map(int, input().split())) for i in range(n)]

    answer = 0
    par = [-1] * n

    edges = []
    for i in range(3):
        sort_coords = sorted(enumerate(coords), key=lambda x: x[1][i])
        for j in range(1, n):
            edges.append((sort_coords[j - 1][0], sort_coords[j][0], sort_coords[j][1][i] - sort_coords[j - 1][1][i]))
    edges = sorted(edges, key=lambda x: x[2])

    for edge in edges:
        if find(edge[0]) != find(edge[1]):
            answer += edge[2]
            if par[find(edge[0])] <= par[find(edge[1])]:
                par[find(edge[0])] += par[find(edge[1])]
                par[find(edge[1])] = find(edge[0])
            else:
                par[find(edge[1])] += par[find(edge[0])]
                par[find(edge[0])] = find(edge[1])   
    print(answer)
