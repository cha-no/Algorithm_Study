
'''

백준 문제

https://www.acmicpc.net/problem/1541

'''


s = input()

l = s.split('-')
answer = sum(list(map(int, l[0].split('+')))) if '+' in l[0] else int(l[0]) 
for eles in l[1:]:
    answer -= sum(list(map(int, eles.split('+')))) if '+' in eles else int(eles) 
print(answer)
