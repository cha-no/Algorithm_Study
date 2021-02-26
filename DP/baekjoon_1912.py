
'''

백준 문제

https://www.acmicpc.net/problem/1912

'''

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if not i:
        index = i
        m = arr[i]
        answer = m
    else:
        if m >= 0:
            m += arr[i]
            answer = max(answer, m)
        else:
            index = i
            m = arr[i]
            answer = max(answer, m)

print(answer)
