'''

백준 문제

https://www.acmicpc.net/problem/2565

'''

n = int(input())

pair_dict = dict()

for i in range(n):
    n1, n2 = list(map(int, input().split()))
    pair_dict[n1] = n2

dp = [0] * (n + 1)
d = [0]
arr = [0] + [n2 for n1, n2 in sorted(pair_dict.items(), key = lambda x : x[0])]

answer = 0

for i in range(1, n + 1):
    if d[-1] < arr[i]:
        answer += 1
        dp[i] = answer
        d.append(arr[i])
    else:
        s, e = 0, answer
        index = 0
        while s <= e:
            m = (s + e) // 2

            if d[m] < arr[i]:
                s = m + 1
                index = max(index, m)
            else:
                e = m - 1
        
        dp[i] = index + 1
        d[index + 1] = min(d[index + 1], arr[i])

print(n - answer)
