'''

백준 문제

https://www.acmicpc.net/problem/10844

'''

n = int(input())

prev = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(n-1):
    cur = [0]*10
    for j in range(10):
        if not j:
            cur[j] = prev[j+1]
        elif j==9:
            cur[j] = prev[j-1]
        else:
            cur[j] = prev[j-1] + prev[j+1]
    cur, prev = prev, cur

print(sum(prev)%1000000000)
