
'''

백준 문제

https://www.acmicpc.net/problem/1021

'''

from collections import deque

def left_distance(queue : deque, target : int) -> int:
    d = 1
    for i in range(len(queue) - 1, -1, -1):
        if queue[i] == target:
            break
        d += 1
    return d

def oper2(queue : deque, count : int) -> None:
    for _ in range(count):
        item = queue.popleft()
        queue.append(item)

def oper3(queue : deque, count : int) -> None:
    for _ in range(count):
        item = queue.pop()
        queue.appendleft(item)    

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    l = list(map(int, input().split()))

    answer = 0
    queue = deque([i + 1 for i in range(n)])

    for i in l:
        count = left_distance(queue, i)
        if count > n // 2:
            count = n - count
            oper2(queue, count)
        else:
            oper3(queue, count)
        queue.popleft()
        answer += count
        n -= 1

    print(answer)
