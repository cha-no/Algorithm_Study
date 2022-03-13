
'''

백준 문제

https://www.acmicpc.net/problem/1311

'''

MAX = 1e9

def dfs(bit, cur):
    if bit == (1 << N) - 1: return 0
    
    if dp[bit][cur]: return dp[bit][cur]
    
    dp[bit][cur] = MAX
    for i in range(N):
        if not bit & (1 << i):
            dp[bit][cur] = min(dp[bit][cur], dfs(bit | (1 << i), cur + 1) + D[cur][i])

    return dp[bit][cur]
    
if __name__ == "__main__":
    N = int(input())
    D = [list(map(int, input().split())) for i in range(N)]
    
    dp = [[0]*N for i in range(1 << N)]
    print(dfs(0, 0))
