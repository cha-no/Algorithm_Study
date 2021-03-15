
'''

백준 문제

https://www.acmicpc.net/problem/11047

'''

n, k = list(map(int, input().split()))
a = [int(input()) for _ in range(n)]

answer = 0

for i in range(n - 1, -1, -1):    
    answer += k // a[i]
    k -= (k // a[i]) * a[i]

print(answer)
