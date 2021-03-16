
'''

백준 문제

https://www.acmicpc.net/problem/1991

'''

from typing import List

class Node(object):
    def __init__(self, item : str) -> None:
        self.__item = item
        self.left = None
        self.right = None
    
    @property
    def item(self):
        return self.__item

class Bst(object):
    def __init__(self) -> None:
        self.__arr = [None] * 26
        
    def init(self, n : int) -> None:
        for i in range(n):
            self.__arr[i] = Node(chr(ord('A') + i))
    
    def insert(self, p : str, l : str, r : str) -> None:
        if l != '.':
            self.__arr[ord(p) - ord('A')].left = self.__arr[ord(l) - ord('A')]
        if r != '.':
            self.__arr[ord(p) - ord('A')].right = self.__arr[ord(r) - ord('A')]
    
    def _preorder(self, node : Node, pre_list : List) -> None:
        if node:
            pre_list.append(node.item)
            self._preorder(node.left, pre_list)
            self._preorder(node.right, pre_list)

    def preorder(self) -> str:
        pre_list = []
        self._preorder(self.__arr[0], pre_list)
        return ''.join(pre_list)

    def _inorder(self, node : Node, i_list : List) -> None:
        if node:
            self._inorder(node.left, i_list)
            i_list.append(node.item)
            self._inorder(node.right, i_list)

    def inorder(self) -> str:
        i_list = []
        self._inorder(self.__arr[0], i_list)
        return ''.join(i_list)

    def _postorder(self, node : Node, post_list : List) -> None:
        if node:
            self._postorder(node.left, post_list)
            self._postorder(node.right, post_list)
            post_list.append(node.item)

    def postorder(self) -> str:
        post_list = []
        self._postorder(self.__arr[0], post_list)
        return ''.join(post_list)

if __name__ == "__main__":
    n = int(input())

    bst = Bst()
    bst.init(n)

    for i in range(n):
        p, l, r = input().split()
        bst.insert(p, l, r)

    print(bst.preorder())
    print(bst.inorder())
    print(bst.postorder())
