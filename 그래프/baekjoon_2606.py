
'''
백준 문제

https://www.acmicpc.net/problem/2606

'''

answer = 0

def dfs(vertex : int) -> None:
    global answer
    if not visit[vertex]:
        visit[vertex] = 1
        answer += 1
        for v in graph[vertex]:
            dfs(v)

if __name__ == "__main__":
    n = int(input())
    e = int(input())

    graph = [[] for i in range(n)]
    for i in range(e):
        v1, v2 = list(map(int, input().split()))
        graph[v1 - 1].append(v2 - 1)
        graph[v2 - 1].append(v1 - 1)

    visit = [0] * n

    dfs(0)
    print(answer - 1)
