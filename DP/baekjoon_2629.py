
'''

백준 문제

https://www.acmicpc.net/problem/2629

'''



n = int(input())
weights = list(map(int, input().split()))
m = int(input())
beads = list(map(int, input().split()))

answer = []
prev, cur = set(), set()
possible = set()
visit = set()

for weight in weights:
    for left, right in prev:
        if right + weight - left > 0:
            possible.add(right + weight - left)
        if right - left - weight > 0:
            possible.add(right - left - weight)

        cur.add((right + weight, left))
        cur.add((right, left + weight))
    if weight not in visit:
        cur.add((weight, 0))
        cur.add((0, weight))
        possible.add(weight)
    visit.add(weight)
    prev, cur = cur, prev

for bead in beads:
    answer += ['Y' if bead in possible else 'N']

print(' '.join(answer))
