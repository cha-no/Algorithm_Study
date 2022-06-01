
'''

백준 문제

https://www.acmicpc.net/problem/14003

'''


def binary_search(s: int, e: int, target: int) -> int:
    while s <= e:
        m = (s + e) // 2
        if lis[m] < target:
            s = m + 1
        else:
            e = m - 1
    return s

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    ind = [0] * n
    lis = [0] * n
    index = 0
    lis[index] = arr[0]
    ind[0] = index

    for i in range(1, n):
        if arr[i] > lis[index]:
            index += 1
            lis[index] = arr[i]
            ind[i] = index
        else:
            idx = binary_search(0, index, arr[i])
            lis[idx] = arr[i]
            ind[i] = idx

    print(index + 1)
    cur_idx = n - 1
    ind_idx = index + 1
    answer = []

    while cur_idx >= 0:
        if ind[cur_idx] == ind_idx - 1:
            answer.append(arr[cur_idx])
            ind_idx = ind[cur_idx]
        cur_idx -= 1

    print(' '.join(map(str, reversed(answer))))
