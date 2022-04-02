
'''

백준 문제

https://www.acmicpc.net/problem/1038

'''

def next_num(n: int) -> int:
    if n == 9876543210: return -1
    str_n = str(n)
    for i in range(len(str_n)):
        if i == len(str_n) - 1:
            if str_n[0] == '9':
                next_n = ''
                for j in range(len(str_n), -1, -1):
                    next_n += str(j)
                next_n = int(next_n)
            else:
                next_n = str(int(str_n[0]) + 1)
                for j in range(len(str_n) - 2, -1, -1):
                    next_n += str(j)
                next_n = int(next_n)
        else:
            if int(str_n[-i - 2]) > int(str_n[-i - 1]) + 1:
                next_n = ''
                for j in range(-len(str_n), -i - 1):
                    next_n += str_n[j]
                next_n += str(int(str_n[-i - 1]) + 1)
                for j in range(i - 1, -1, -1):
                    next_n += str(j)
                next_n = int(next_n)
                break
    return next_n

if __name__ == "__main__":
    n = int(input())
    answer = 0
    order = 0

    while order < n:
        answer = next_num(answer)
        order += 1
        if answer == -1: break
    
    print(answer)
