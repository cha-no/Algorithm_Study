'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

'''

def maxMin(k, n, arr):
    arr.sort()
    m = arr[-1]
    for i in range(n-k+1):
        if arr[i+k-1] - arr[i] < m:
            m = arr[i+k-1] - arr[i]
    return m
