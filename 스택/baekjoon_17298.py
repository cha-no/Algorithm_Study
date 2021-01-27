'''

백준 문제

https://www.acmicpc.net/problem/17298

'''

n = int(input())
a = list(map(int, input().split()))

stack = [0]
nge = [-1] * n

for i in range(1, n):
    if a[i-1] < a[i]:
        while stack:
            if a[stack[-1]] < a[i]:
                nge[stack.pop()] = a[i]
                continue
            break
    stack.append(i)
    
print(' '.join(list(map(str, nge))))
