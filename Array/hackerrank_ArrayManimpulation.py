'''

hackerrank 문제

난이도 : hard

https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

'''

def arrayManipulation(n, queries):
    answer = 0
    value = 0
    arr = [0 for i in range(n)]
    for query in queries:
        arr[query[0]-1] += query[2]
        if query[1] == n:
            continue
        arr[query[1]] -= query[2]
    for i in arr:
        value += i
        if value > answer:
            answer = value 
    return answer
