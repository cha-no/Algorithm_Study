'''

백준 문제

https://www.acmicpc.net/problem/1874

'''

n = int(input())
seq = []

for i in range(n):
    seq.append(int(input()))

stack = []
order = []
oper = []
flag = True

while seq:
    ele = seq.pop()
    if not stack or stack[-1] < ele:
        stack.append(ele)
        oper.append('-')
    else:
        while stack and stack[-1] > ele:
            order.append(stack.pop())
            oper.append('+')
        stack.append(ele)
        oper.append('-')

while stack:
    order.append(stack.pop())
    oper.append('+')

for i in range(n-1):
    if order[i] < order[i+1]:
        flag = False
        break

if flag:
    while oper:
        print(oper.pop())
else:
    print('NO')
