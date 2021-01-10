'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

'''

def superDigit(n, k):
    def check(n):
        if n < 10:
            return n
        temp = 0
        while n!=0:
            temp += n%10
            n //= 10
        return check(temp)
    num = 0
    for i in n:
        num += int(i)
    return check(num*k)
