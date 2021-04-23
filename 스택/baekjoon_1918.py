
'''
백준 문제

https://www.acmicpc.net/problem/1918

'''

push_order = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '(' : 4,
    ')' : 3
}
pop_order = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '(' : 0,
    ')' : 3
}

infix = input()
postfix = ''
stack = []


for s in infix:
    if 65 <= ord(s) <= 90:
        postfix += s
    elif s == ')':
        while stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    else:
        while stack and pop_order[stack[-1]] >= push_order[s]:
            postfix += stack.pop()
        stack.append(s)

while stack:
    postfix += stack.pop()
    
print(postfix)
