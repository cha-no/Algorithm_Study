
'''

백준 문제

https://www.acmicpc.net/problem/1300

'''

n = int(input())
k = int(input())

answer = n ** 2 + 1
s, e = 1, k

while s <= e:
    m = (s + e) // 2
    
    c = 0
    for i in range(1, n + 1):
        c += min(n, m // i)
    
    if c < k:
        s = m + 1
    else:
        e = m - 1
        answer = min(answer, m)

print(answer)
