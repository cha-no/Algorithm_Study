
'''

백준 문제

https://www.acmicpc.net/problem/13913

'''


from collections import deque

def is_possible(n: int) -> bool:
    return 0 <= n <= 100000

if __name__ == "__main__":
    n, k = map(int, input().split())
    
    visit = [False] * 100001
    dp = [-1] * 100001

    visit[n] = True
    queue = deque([(n, 0)])

    while queue:
        m, t = queue.popleft()
        if m == k:
            break
        
        if is_possible(m + 1) and not visit[m + 1]:
            visit[m + 1] = True
            dp[m + 1] = m
            queue.append((m + 1, t + 1))
        if is_possible(m - 1) and not visit[m - 1]:
            visit[m - 1] = True
            dp[m - 1] = m
            queue.append((m - 1, t + 1))
        if is_possible(2 * m) and not visit[2 * m]:
            visit[2 * m] = True
            dp[2 * m] = m
            queue.append((2 * m, t + 1))

    print(t)
    trace = ''
    while m >= 0:
        trace = ' ' + str(m) + trace
        m = dp[m]
    print(trace.strip())
