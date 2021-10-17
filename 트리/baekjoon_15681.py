
'''

백준 문제

https://www.acmicpc.net/problem/15681

'''



import sys

def makeTree(node : int, parent : int) -> None :
    global tree
    for u in connect[node] :
        if u == parent : continue
        tree[node].append(u)
        makeTree(u, node)

def getNodeNumber(node : int) -> None :
    global dp
    dp[node] = 1
    for u in tree[node] :
        getNodeNumber(u)
        dp[node] += dp[u]
        
if __name__ == "__main__" :
    sys.setrecursionlimit(1000000)
    global dp, tree
    n, r, q = list(map(int, sys.stdin.readline().split()))

    connect = [[] for i in range(n)]

    for i in range(n - 1) :
        u, v = list(map(int, sys.stdin.readline().split()))
        connect[u - 1].append(v - 1)
        connect[v - 1].append(u - 1)
        
    dp = [0] * n
    tree = [[] for i in range(n)]
    
    makeTree(r - 1, -1)
    getNodeNumber(r - 1)
    
    for i in range(q) :
        query = int(sys.stdin.readline())
        print(dp[query - 1])
