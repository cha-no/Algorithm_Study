
'''

백준 문제

https://www.acmicpc.net/problem/4949

'''


f = True

while True:
    s = input()
    if s=='.':
        break
    
    if f:
        flag = True
        stack = []
        f = False
    
    for i in s:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if not stack or stack[-1]!='(':
                flag = False
                break
            else:
                stack.pop()
        elif i==']':
            if not stack or stack[-1]!='[':
                flag = False
                break
            else:
                stack.pop()
    
    if s[-1]=='.':
        if flag and not stack:
            print('yes')
        else:
            print('no')
        f = True
