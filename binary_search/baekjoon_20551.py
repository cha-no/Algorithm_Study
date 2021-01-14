'''

백준 문제

https://www.acmicpc.net/problem/20551

'''


import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

for i in range(M):
    query = int(sys.stdin.readline())
    flag = True
    s, e = 0, N-1
    ans = 2*100000 + 1
    if query < arr[s] or query > arr[e]:
        print(-1)
        continue
    while s<=e:
        m = (s+e)//2
        if arr[m]==query:
            ans = min(ans, m)
            e = m-1
            flag = False
        elif arr[m]<query:
            s = m+1
        else:
            e = m-1
    if flag:
        print(-1)
    else:
        print(ans)
