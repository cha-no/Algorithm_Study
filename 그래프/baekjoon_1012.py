
'''

백준 문제

https://www.acmicpc.net/problem/1012

'''



def isPossible(x : int, y : int, m : int, n : int) -> bool:
    return 0 <= x < m and 0 <= y < n


if __name__ == "__main__":
    t = int(input())

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for _ in range(t):
        m, n, k = list(map(int, input().split()))
        cabbages = [list(map(int, input().split())) for i in range(k)]

        maps = [[0] * n for i in range(m)]
        visit = [[0] * n for i in range(m)]

        answer = 0
        stack = []

        for x, y in cabbages:
            maps[x][y] = 1

        for i in range(m):
            for j in range(n):
                if visit[i][j] or not maps[i][j]:
                    continue

                answer += 1
                stack.append((i, j))

                while stack:
                    x, y = stack.pop()

                    for k in range(4):
                        new_x, new_y = x + dx[k], y + dy[k]
                        if isPossible(new_x, new_y, m, n) and not visit[new_x][new_y] and maps[new_x][new_y]:
                            visit[new_x][new_y] = 1
                            stack.append((new_x, new_y))

        print(answer)
