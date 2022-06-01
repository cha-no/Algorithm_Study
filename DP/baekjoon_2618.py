
'''

백준 문제

https://www.acmicpc.net/problem/2618

'''

import sys
sys.setrecursionlimit(10**9)

def l1_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)

def dfs(a: int, b:int) -> None:
    if a == w or b == w: return 0
    if dp[a][b] != -1: return dp[a][b]

    acc_idx = max(a, b) + 1
    if not a:
        x1, y1 = 1, 1
        x2, y2 = accidents[acc_idx - 1]
        distance_a = l1_distance(x1, y1, x2, y2)
    else:
        x1, y1 = accidents[a - 1]
        x2, y2 = accidents[acc_idx - 1]
        distance_a = l1_distance(x1, y1, x2, y2)
    if not b:
        x1, y1 = n, n
        x2, y2 = accidents[acc_idx - 1]
        distance_b = l1_distance(x1, y1, x2, y2)
    else:
        x1, y1 = accidents[b - 1]
        x2, y2 = accidents[acc_idx - 1]
        distance_b = l1_distance(x1, y1, x2, y2)

    total_a = dfs(acc_idx, b) + distance_a
    total_b = dfs(a, acc_idx) + distance_b
    if total_a < total_b:
        dp[a][b] = total_a
    else:
        dp[a][b] = total_b
    return dp[a][b]

def trace(a: int, b: int) -> None:
    if a == w or b == w: return

    acc_idx = max(a, b) + 1
    if not a:
        x1, y1 = 1, 1
        x2, y2 = accidents[acc_idx - 1]
        distance_a = l1_distance(x1, y1, x2, y2)
    else:
        x1, y1 = accidents[a - 1]
        x2, y2 = accidents[acc_idx - 1]
        distance_a = l1_distance(x1, y1, x2, y2)
    if not b:
        x1, y1 = n, n
        x2, y2 = accidents[acc_idx - 1]
        distance_b = l1_distance(x1, y1, x2, y2)
    else:
        x1, y1 = accidents[b - 1]
        x2, y2 = accidents[acc_idx - 1]
        distance_b = l1_distance(x1, y1, x2, y2)

    if dp[acc_idx][b] + distance_a < dp[a][acc_idx] + distance_b:
        print(1)
        trace(acc_idx, b)
    else:
        print(2)
        trace(a, acc_idx)

if __name__ == "__main__":
    n, w = int(input()), int(input())
    accidents = [list(map(int, input().split())) for i in range(w)]

    dp = [[-1] * (w + 1) for i in range(w + 1)]

    print(dfs(0, 0))
    trace(0, 0)
