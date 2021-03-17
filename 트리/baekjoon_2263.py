
'''

백준 문제

https://www.acmicpc.net/problem/2263

'''

import sys
sys.setrecursionlimit(10**8)

def preorder_travel(i_l : int, i_r : int, p_l : int, p_r : int) -> None:
    if i_l > i_r or p_l > p_r:
        return
    
    root = postorder[p_r]
    right = pos_list[root - 1]
    
    preorder.append(root)
    
    preorder_travel(i_l, right - 1, p_l, p_l + right - i_l - 1)
    preorder_travel(right + 1, i_r, p_l + right - i_l, p_r - 1)

if __name__ == "__main__":
    n = int(input())

    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    preorder = []
    pos_list = [0] * n
    
    for i in range(n):
        pos_list[inorder[i] - 1] = i

    preorder_travel(0, n - 1, 0, n - 1)

    print(' '.join(list(map(str, preorder))))
