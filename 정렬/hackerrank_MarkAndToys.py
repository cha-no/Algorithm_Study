'''

hackerrank 문제

난이도 : easy

https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

'''

def maximumToys(prices, k):
    total = 0
    answer = 0
    prices.sort()
    for price in prices:
        total += price
        if total > k:
            break
        answer+=1
    return answer
