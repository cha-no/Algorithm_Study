
'''

백준 문제

https://www.acmicpc.net/problem/1949

'''


import sys

sys.setrecursionlimit(10**9)

def dfs(v: int) -> None:
    if visit[v]: return
    visit[v] = 1
    
    dp1, dp2 = 0, 0
    for u in tree[v]:
        dfs(u)
        dp1 += max(dp[u][0], dp[u][1])
        dp2 += dp[u][0]
    
    dp[v][0] = dp1
    dp[v][1] = dp2 + peoples[v]

if __name__ == "__main__":
    N = int(input())
    peoples = list(map(int, input().split()))
    tree = [[] for i in range(N)]

    for i in range(N - 1):
        u, v = map(int, input().split())
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    dp = [[0, 0] for i in range(N)]
    visit = [0] * N

    dfs(0)
    print(max(dp[0]))
