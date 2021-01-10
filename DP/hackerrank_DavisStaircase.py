'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

'''

def stepPerms(n):
    f = {}
    for i in range(1,n+1):
        if i == 1:
            f[1] = 1
        elif i == 2:
            f[2] = 2
        elif i == 3:
            f[3] = 4
        else:
            f[i] = f[i-1] + f[i-2] + f[i-3]
    return f[n]
