'''

백준 문제

https://www.acmicpc.net/problem/1920

'''


n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()

for i in b:
    s, e = 0, n-1
    if i<a[s] or i>a[e]:
        print(0)
        continue
    flag = False
    while s<=e:
        m = (s + e)//2
        if a[m]>i:
            e = m-1
        elif a[m]<i:
            s = m+1
        else:
            flag = True
            break
    if flag:
        print(1)
    else:
        print(0)
