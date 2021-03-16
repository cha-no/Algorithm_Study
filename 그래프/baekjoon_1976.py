
'''

백준 문제

https://www.acmicpc.net/problem/1976

'''

def find(k : int) -> int:
    return k if par[k] < 0 else find(par[k])

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    plan = list(map(int, input().split()))

    par = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if graph[j][i] and find(i) != find(j):
                if find(i) <= find(j):
                    par[find(i)] = find(j)
                else:
                    par[find(j)] = find(i)

    poss = set()
    for i in plan:
        poss.add(find(i - 1))
        if len(poss) > 1:
            break

    answer = 'YES' if len(poss) == 1 else 'NO'
    print(answer)
