'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

'''

def countTriplets(arr, r):
    answer = 0
    arr_dict = {}
    pair_dict = {}
    for i in arr[::-1]:
        arr_dict[i] = arr_dict.get(i,0)+1
        if i*r in pair_dict:
            answer += pair_dict[i*r]
        if i*r in arr_dict:
            pair_dict[i] = pair_dict.get(i,0) + arr_dict[i*r]
    
    if r==1:
        answer = 0
        for i in arr_dict:
            n = arr_dict[i]
            if n>=3:
                answer += int(n*(n-1)*(n-2)/6)
    return answer
