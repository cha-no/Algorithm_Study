'''

백준 문제

https://www.acmicpc.net/problem/13305

'''

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

answer = 0
cost = costs[0]

for i in range(1, n):
    answer += roads[i - 1] * cost
    if costs[i] < cost:
        cost = costs[i]

print(answer)
