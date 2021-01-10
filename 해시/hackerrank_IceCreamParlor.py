'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

'''

def whatFlavors(cost, money):
    cost_dict = {}
    for i, c in enumerate(cost):
        other = money - c
        if other in cost_dict:
            print(cost_dict[other]+1,i+1)
            return
        else:
            cost_dict[c] = i
