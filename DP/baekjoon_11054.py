
'''

백준 문제

https://www.acmicpc.net/problem/11054

'''

n = int(input())
a = list(map(int, input().split()))

dp_min = [0] * n
dp_max = [0] * n

for i in range(n):
    min_value = 0
    max_value = 0
    for j in range(i):
        if a[i] > a[j]:
            min_value = max(min_value, dp_min[j])
        if a[i] < a[j]:
            max_value = max(max_value, dp_max[j])
    dp_min[i] = min_value + 1
    dp_max[i] = max(min_value, max_value) + 1
print(max(dp_max))
