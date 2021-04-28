
'''

백준 문제

https://www.acmicpc.net/problem/5639

'''


import sys
from typing import List

sys.setrecursionlimit(20000)

def find_post(preorder : List[int]) -> None:
    root = preorder[0]
    postorder.append(root)
    
    right = -1
    
    for i in range(1, len(preorder)):
        if preorder[i] > root:
            right = i
            break
                
    if len(preorder) > 1:
        if right > 1:
            find_post(preorder[right:])
            find_post(preorder[1:right])
        elif right == 1:
            find_post(preorder[right:])
        else:
            find_post(preorder[1:])
        

if __name__ == "__main__":
    preorder = []
    postorder = []

    while True:
        try:
            num = input()
        except:
            break

        preorder.append(int(num))

    find_post(preorder)
    
    print(' '.join(map(str, reversed(postorder))))
