
'''

백준 문제

https://www.acmicpc.net/problem/7579

'''



from copy import deepcopy

n, m = list(map(int, input().split()))
apps = list(map(int, input().split()))
costs = list(map(int, input().split()))

prev, cur = {0: 0}, {0: 0}

for cost, app in zip(costs, apps):
    for k, v in prev.items():
        cur[cost + k] = prev.get(cost + k, 0)
        cur[cost + k] = max(cur[cost + k], app + v)
    prev = deepcopy(cur)

for i, (k, v) in enumerate(sorted(prev.items())):
    if not i:
        before = v
        continue
    if v < before:
        cur.pop(k)
    before = v

for k, v in sorted(cur.items()):
    if v >= m:
        answer = k
        break
print(answer)
