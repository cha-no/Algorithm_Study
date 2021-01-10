'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

'''

def getMinimumCost(n, k, c):
    c = sorted(c, reverse = True)
    index = 0
    pur = 0
    answer = 0
    while True:
        if n <= k:
            answer += (pur + 1)*sum(c[index:index+n])
            break
        answer += (pur + 1)*sum(c[index:index+k])
        pur += 1
        index += k
        n -= k
    return answer
