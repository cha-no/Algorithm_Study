
'''

백준 문제

https://www.acmicpc.net/problem/16928

'''


from collections import deque

n, m = map(int, input().split())

ladder_map = {}
snake_map = {}
for i in range(n):
    x, y = map(int, input().split())
    ladder_map[x] = y
for i in range(m):
    u, v = map(int, input().split())
    snake_map[u] = v

answer = 101

queue = deque([(1, 0)])
visit = [False] * 101
visit[1] = True

while queue:
    u, cur = queue.popleft()

    for dice in range(1, 7):
        new_u = u + dice
        if new_u == 100:
            answer = min(answer, cur + 1)
            break

        if new_u in ladder_map:
            new_u = ladder_map[new_u]
        elif new_u in snake_map:
            new_u = snake_map[new_u]
        if new_u > 100 or visit[new_u]: continue

        visit[new_u] = True
        queue.append((new_u, cur + 1))

print(answer)
