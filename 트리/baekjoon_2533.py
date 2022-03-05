
'''

백준 문제

https://www.acmicpc.net/problem/2533

'''

import sys

sys.setrecursionlimit(10**9)

def dfs(v: int, depth: int) -> None:
    global dp, visit
    if visit[v]: return
    visit[v] = 1
    
    dp1, dp2 = 0, 0
    for u in tree[v]:
        dfs(u, depth + 1)
        dp1 += min(dp[u][0], dp[u][1])
        dp2 += dp[u][0]
    
    dp[v][0] = dp1 + 1
    dp[v][1] = dp2



if __name__ == "__main__":
    n = int(sys.stdin.readline())
    tree = [[] for i in range(n)]

    for i in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)
        
    dp = [[0, 0] for i in range(n)]
    visit = [0] * n
    
    dfs(0, 0)

    answer = min(dp[0])
    print(answer)
