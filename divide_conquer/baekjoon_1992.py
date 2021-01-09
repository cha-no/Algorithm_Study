'''

백준 문제

https://www.acmicpc.net/problem/1992

'''


def divide(video):
    n = len(video)
    c = video[0][0]
    flag = True
    for i in range(n):
        for j in range(n):
            if c!=video[i][j]:
                flag = False
                break
        if not flag:
            print('(',end = '')
            for k in range(4):
                temp = []
                for sub in video[(k//2)*(n//2):(k//2)*(n//2)+(n//2)]:
                    temp.append(sub[(k%2)*(n//2):(k%2)*(n//2)+(n//2)])
                divide(temp)
            print(')',end = '')
            break
    if flag:
        print(c, end = '')

n = int(input())
video = []

for i in range(n):
    video.append(input())

divide(video)
