'''

백준 문제

https://www.acmicpc.net/problem/1966

'''

from collections import deque

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n, m = list(map(int, input().split()))
        docs = list(map(int, input().split()))

        queue = deque([])
        index = 0
        for doc in docs:
            queue.append((index, doc))
            index += 1

        answer = 0
        while queue:
            (index, doc) = queue.popleft()
            for (i, d) in queue:
                if doc < d:
                    queue.append((index,doc))
                    break
            else:
                answer += 1
                if index == m:
                    break

        print(answer)
