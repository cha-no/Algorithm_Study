
'''

백준 문제

https://www.acmicpc.net/problem/1931

'''

n = int(input())

conferences = []
answer = 0
end = 0

for i in range(n):
    conference = list(map(int, input().split()))
    conferences.append(conference)

for (s, e) in sorted(conferences, key = lambda x: (x[1], -x[0])):
    if end <= s:
        answer += 1
        end = e

print(answer)
