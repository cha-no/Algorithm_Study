
'''

백준 문제

https://www.acmicpc.net/problem/12015

'''

n = int(input())
a = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
d = [0]

answer = 0
for i in range(1, n + 1):
    if d[-1] < a[i]:
        answer += 1
        dp[i] = answer
        d.append(a[i])
    else:
        s, e = 0, answer
        index = 0
        
        while s <= e:
            m = (s + e) // 2
            if d[m] < a[i]:
                s = m + 1
                index = max(index, m)
            else:
                e = m - 1
        
        dp[i] = index + 1
        d[index + 1] = min(d[index + 1], a[i])

print(answer)
