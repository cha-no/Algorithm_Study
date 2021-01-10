'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

'''

def isBalanced(s):
    stack = []
    for i in s:
        if i=='(' or i=='[' or i=='{':
            stack.append(i)
        else:
            try:
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return 'NO'
            except:
                return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'
