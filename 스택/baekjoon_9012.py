
'''

백준 문제

https://www.acmicpc.net/problem/9012

'''

t = int(input())

for i in range(t):
    s = input()
    stack = []

    check = True
    for b in s:
        if b == '(':
            stack.append(b)
        else:
            if stack:
                stack.pop()
            else:
                check = False
                break
    if stack:
        check = False
    
    answer = 'YES' if check else 'NO'
    print(answer)
