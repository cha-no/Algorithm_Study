
'''

백준 문제

https://www.acmicpc.net/problem/20040

'''

import sys

def find(u : int) -> int:
    return u if par[u] < 0 else find(par[u])

if __name__ == "__main__":
    n, m = list(map(int, sys.stdin.readline().split()))

    par = [-1] * n
    flag = False
    answer = 0

    for c in range(m):
        u, v = list(map(int, sys.stdin.readline().split()))
        if flag:
            continue
        if find(u) == find(v):
            answer = c + 1
            flag = True
        else:
            if par[find(u)] <= par[find(v)]:
                par[find(u)] += par[find(v)]
                par[find(v)] = find(u)
            else:
                par[find(v)] += par[find(u)]
                par[find(u)] = find(v)
    print(answer)
