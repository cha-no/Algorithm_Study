
'''

백준 문제

https://www.acmicpc.net/problem/9663

'''
    
def queen(h : int) -> None:
    global answer
    if h == n:
        answer += 1
        return
    
    for w in range(n):
        if w in col or w + h in diag1 or w - h in diag2:
            continue
        col.add(w)
        diag1.add(w + h)
        diag2.add(w - h)
        queen(h + 1)
        col.remove(w)
        diag1.remove(w + h)
        diag2.remove(w - h)

if __name__ == "__main__":
    n = int(input())
    answer = 0
    col = set()
    diag1 = set()
    diag2 = set()
    queen(0)
    print(answer)
