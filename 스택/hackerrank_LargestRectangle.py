'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

'''

def largestRectangle(h):
    i, m = 0, 0
    stack = []
    while(i < len(h)):
        if not stack or h[stack[-1]] <= h[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if stack:
                m = max(m, h[top]*(i-stack[-1]-1))
            else:
                m = max(m, h[top]*i)
    while stack:
        top = stack.pop()
        if stack:
            m = max(m, h[top]*(i-stack[-1]-1))
        else:
            m = max(m, h[top]*i)
    return m
