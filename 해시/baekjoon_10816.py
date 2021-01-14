'''

백준 문제

https://www.acmicpc.net/problem/10816

'''

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

answer = ''
num_dict = {}
for num in nums:
    num_dict[num] = num_dict.get(num, 0) + 1

for find in finds:
    answer += str(num_dict.get(find, 0)) + ' '
print(answer.strip())
