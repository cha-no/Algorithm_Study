
'''

백준 문제

https://www.acmicpc.net/problem/12852

'''


from collections import deque

def is_valid(n: int) -> bool:
    return n > 0

if __name__ == "__main__":
    n = int(input())
    visit = [False] * (n + 1)
    dp = [0] * (n + 1)
    visit[n] = True
    queue = deque([(n, 0)])

    while queue:
        s, c = queue.popleft()
        if s == 1:
            break

        if not s % 3 and not visit[s // 3]:
            visit[s // 3] = True
            dp[s // 3] = s
            queue.append((s // 3, c + 1))
        if not s % 2 and not visit[s // 2]:
            visit[s // 2] = True
            dp[s // 2] = s
            queue.append((s // 2, c + 1))        
        if is_valid(s - 1) and not visit[s - 1]:
            visit[s - 1] = True
            dp[s - 1] = s
            queue.append((s - 1, c + 1))        

    print(c)
    s = 1
    trace = ''
    while s != 0:
        trace = ' ' + str(s) + trace
        s = dp[s]
    print(trace.strip())
