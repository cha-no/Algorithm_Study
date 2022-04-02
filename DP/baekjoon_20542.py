
'''

백준 문제

https://www.acmicpc.net/problem/20542

'''

error_dict = {
    'i': ['j', 'l'],
    'v': ['w']
}

def isSame(s: str, t: str) -> bool:
    if s == t: return True
    elif s in error_dict and t in error_dict[s]: return True
    else: return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    source, target = input(), input()
    
    dp = [[0] * (m + 1) for i in range(n + 1)]
    
    for i in range(1, n + 1): dp[i][0] = i
    for j in range(1, m + 1): dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if isSame(source[i - 1], target[j - 1]): dp[i][j] = dp[i - 1][j - 1]
            else: dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    print(dp[n][m])
