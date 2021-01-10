'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

'''

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        pass
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0
