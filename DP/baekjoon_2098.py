
'''

백준 문제

https://www.acmicpc.net/problem/2098

'''

MAX = 16 * 1000000 + 1
START = 0

def dfs(bit: int, cur: int) -> int:
    global START
    if bit == (1 << n) - 1:
        if w[cur][START]: return w[cur][START]
        else: return MAX
        
    if dp[bit][cur]: return dp[bit][cur]
    
    dp[bit][cur] = MAX
    for i in range(n):
        if not bit & (1 << i) and i != cur and w[cur][i]:
            dp[bit][cur] = min(dp[bit][cur], dfs(bit | (1 << i), i) + w[cur][i])

    return dp[bit][cur]

if __name__ == "__main__":
    n = int(input())
    w = [list(map(int, input().split())) for i in range(n)]
    
    dp = [[0]*n for i in range(1 << n)]
    print(dfs(1 << START, START))
