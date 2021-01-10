'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

'''

def minimumSwaps(arr):
    n = len(arr)
    answer = 0
    index = 0
    while True:
        if n==index:
            break
        if arr[index] == index+1:
            index += 1
            continue
        temp = arr[index]-1
        arr[index], arr[temp] = arr[temp], arr[index]
        answer += 1
    return answer
