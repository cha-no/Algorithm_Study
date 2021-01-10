'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

'''

def pairs(k, arr):
    answer = 0
    arr_dict = {}
    arr.sort()
    for i in arr:
        arr_dict[i] = arr_dict.get(i, 0) + 1
        if i-k in arr_dict:
            answer += 1 
    return answer
