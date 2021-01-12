'''

백준 문제

https://www.acmicpc.net/problem/1717

'''

import sys

def find(v):
    return v if par[v]<0 else find(par[v])

if __name__== "__main__":
    n, m = list(map(int, sys.stdin.readline().split()))

    par = [-1]*(n+1)

    for i in range(m):
        oper = list(map(int, sys.stdin.readline().split()))
        if oper[0]:
            if find(oper[1]) != find(oper[2]):
                print('NO')
            else:
                print('YES')
        else:
            if find(oper[1]) != find(oper[2]):
                if par[find(oper[1])] <= par[find(oper[2])]:
                    par[find(oper[1])] += par[find(oper[2])]
                    par[find(oper[2])] = find(oper[1])
                else:
                    par[find(oper[2])] += par[find(oper[1])]
                    par[find(oper[1])] = find(oper[2])   
