'''

백준 문제

https://www.acmicpc.net/problem/1654

'''
k, n = list(map(int, input().split()))

lans = []
for i in range(k):
    lans.append(int(input()))

s, e = 1, 2 ** 31 - 1
answer = s

while s <= e:
    m = (s + e) // 2
    count = 0
    for lan in lans:
        count += lan // m
    
    if count >= n:
        s = m + 1
        answer = max(answer, m)
    else:
        e = m - 1
print(answer)
