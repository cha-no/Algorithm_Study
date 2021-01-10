'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

'''

def maxSubsetSum(arr, n):
    D = {}
    D[0], D[1] = arr[0], max(arr[0], arr[1])
    for i in range(2,n):
        D[i] = max(D[i-2] + arr[i], D[i-1], arr[i], arr[i-1])
    return D[n-1]
