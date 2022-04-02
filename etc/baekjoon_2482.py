
'''

백준 문제

https://www.acmicpc.net/problem/2482

'''

import sys

sys.setrecursionlimit(10**9)


def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)

def combination(n: int, r: int) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))

def duplicate_combination(n: int, r: int) -> int:
    return combination(n + r - 1, r) if n else 1
    
def color_ring(n: int, k: int) -> int:
    if n / k < 2: print(0)
    else:
        sub = duplicate_combination(k, n - 2 * k)
        print((sub * n // k) % 1000000003)
        
if __name__ == "__main__":
    color_ring(int(input()), int(input()))
