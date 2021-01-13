'''

백준 문제

https://www.acmicpc.net/problem/1197

'''

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
