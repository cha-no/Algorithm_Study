'''

백준 문제

https://www.acmicpc.net/problem/1697

'''

from collections import deque

n, k = list(map(int, input().split()))
visit = {}

MAX = 100000

queue = deque([(n, 0)])

while queue:
    (s, cur) = queue.popleft()
    visit[s] = cur
    if s == k:
        print(cur)
        break
    elif s < k:
        if 2*s <= MAX and not visit.get(2*s,0):
            queue.append((2*s, cur+1))
        if s < MAX and not visit.get(s+1,0):
            queue.append((s+1, cur+1))
    if s and not visit.get(s-1,0):
        queue.append((s-1, cur+1))
