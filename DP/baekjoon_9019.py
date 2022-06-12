
'''

백준 문제

https://www.acmicpc.net/problem/9019

'''

from collections import deque

def D(n: int) -> int:
    return n * 2 % 10000

def S(n: int) -> int:
    return (n - 1) % 10000

def L(n: int) -> int:
    return (n % 1000) * 10 + (n // 1000)

def R(n: int) -> int:
    return (n % 10) * 1000 + (n // 10)

func_dict = {
    'D': D,
    'S': S,
    'L': L,
    'R': R,
}

if __name__ == "__main__":
    t = int(input())
    
    for i in range(t):
        a, b = map(int, input().split())
        visit = [False] * 10000
        visit[a] = True
        queue = deque([(a, '')])

        while queue:
            a, trace = queue.popleft()
            if a == b: break

            for f, func in func_dict.items():
                new_a = func(a)
                if visit[new_a]: continue
                visit[new_a] = True
                queue.append((new_a, trace + f))

        print(trace)
