
'''

백준 문제

https://www.acmicpc.net/problem/2213

'''

def dfs(v : int) -> None:
    global visit, weights
    if visit[v]: return
    visit[v] = 1
    subsize1 = 0
    subset1 = set()
    subsize2 = 0
    subset2 = {v}
    for u in tree[v]:
        dfs(u)
        index = 0 if dp[u][0]['size'] > dp[u][1]['size'] else 1
        subsize1 += dp[u][index]['size']
        subset1.update(dp[u][index]['subset'])
        subsize2 += dp[u][0]['size']
        subset2.update(dp[u][0]['subset'])
    dp[v][0]['size'] = subsize1
    dp[v][0]['subset'] = subset1
    dp[v][1]['size'] = subsize2 + weights[v]
    dp[v][1]['subset'] = subset2

if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))

    tree = [[] for i in range(n)]
    for i in range(n - 1):
        u, v = map(int, input().split())
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)
    
    dp = [[{'size':0, 'subset':set()}, {'size':0, 'subset':set()}] for i in range(n)]
    visit = [0] * n
    
    dfs(0)
    
    index = 0 if dp[0][0]['size'] > dp[0][1]['size'] else 1
    print(dp[0][index]['size'])
    print(' '.join(list(map(lambda x:str(x + 1), sorted(dp[0][index]['subset'])))))
