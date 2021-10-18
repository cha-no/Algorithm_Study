
'''

백준 문제

https://www.acmicpc.net/problem/11723

'''

import sys

m = int(sys.stdin.readline())

check = [0] * 20

for i in range(m) :
    oper = sys.stdin.readline().split()
    if oper[0] == 'add' : check[int(oper[1]) - 1] = 1
    elif oper[0] == 'remove' : check[int(oper[1]) - 1] = 0
    elif oper[0] == 'check' : print(check[int(oper[1]) - 1])
    elif oper[0] == 'toggle' : check[int(oper[1]) - 1] ^= 1
    elif oper[0] == 'all' : check = [1] * 20
    else : check = [0] * 20
