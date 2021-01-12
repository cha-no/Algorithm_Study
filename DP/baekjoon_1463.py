'''

백준 문제

https://www.acmicpc.net/problem/1463

'''

n = int(input())

dp = [0]*n
for i in range(1, n):
    dp[i] = dp[i-1]+1
    if (i+1)%2==0:
        dp[i] = min(dp[i], dp[((i+1)//2)-1]+1)
    if (i+1)%3==0:
        dp[i] = min(dp[i], dp[((i+1)//3)-1]+1)
print(dp[-1])
