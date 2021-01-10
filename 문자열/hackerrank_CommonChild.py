'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

'''

def commonChild(s1, s2):
    n = len(s1)
    cur, prev = [0]*(n+1), [0]*(n+1)

    for i in range(n):
        for j in range(n):
            if s1[i]==s2[j]:
                cur[j+1] = prev[j] + 1
            else:
                if cur[j] > prev[j+1]:
                    cur[j+1] = cur[j]
                else:
                    cur[j+1] = prev[j+1]
        cur,prev = prev,cur
    return prev[n]
