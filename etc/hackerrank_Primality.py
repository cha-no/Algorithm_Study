'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/ctci-big-o/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous

'''

def primality(n):
    flag = 0
    if n==1:
        return 'Not prime'
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            flag = 1
            break
    if flag:
        return 'Not prime'
    else:
        return 'Prime'
