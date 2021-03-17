
'''

백준 문제

https://www.acmicpc.net/problem/2178

'''
    
def isRow(i : int, n : int) -> bool:
    return 0 <= i and i < n

def isCol(j : int, m : int) -> bool:
    return 0 <= j and j < m

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    graph = [list(map(int, list(input()))) for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[100 ** 2 + 1] * m for _ in range(n)]
    stack = [(0, 0, 1)]

    while stack:
        x, y, cost = stack.pop()
        if visit[x][y] <= cost:
            continue

        visit[x][y] = cost
        for i in range(4):
            if not isRow(x + dx[i], n) or not isCol(y + dy[i], m) or not graph[x + dx[i]][y + dy[i]]:
                continue
            stack.append((x + dx[i], y + dy[i], cost + 1))

    print(visit[-1][-1])
