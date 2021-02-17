
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42892?language=python3#

'''

from typing import List, Sequence
import sys
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self, x : int, y : int, num : int) -> None:
        self.x = x
        self.y = y
        self.num = num
        self.left = None
        self.right = None

class BSTree(object):
    def __init__(self) -> None:
        self.root = None
        self.pre_list = []
        self.post_list = []

    def insert(self, x : int, y : int, num : int) -> None:
        node = Node(x, y, num)
        self.root = self._insert(self.root, node)
        
    def _insert(self, root : Node, node : Node) -> Node:
        if root is None:
            root = node
        else:
            if root.x < node.x:
                root.right = self._insert(root.right, node)
            else:
                root.left = self._insert(root.left, node)
        return root
    
    def preorder(self) -> List[int]:
        self._preorder(self.root)
        return self.pre_list
    
    def _preorder(self, root : Node) -> None:
        if root is not None:
            self.pre_list.append(root.num)
            self._preorder(root.left)
            self._preorder(root.right)
    
    def postorder(self) -> List[int]:
        self._postorder(self.root)
        return self.post_list
    
    def _postorder(self, root : Node) -> None:
        if root is not None:
            self._postorder(root.left)
            self._postorder(root.right)
            self.post_list.append(root.num)

def solution(nodeinfo : List[Sequence[int]]) -> List[List]:
    bs_tree = BSTree()
    nodeinfo_sort = [[x, y, i + 1] for i, (x, y) in enumerate(nodeinfo)]
    nodeinfo_sort = sorted(nodeinfo_sort, key = lambda x : (-x[1], x[0]))

    for (x, y, num) in nodeinfo_sort:
        bs_tree.insert(x, y, num)
    
    return [bs_tree.preorder(), bs_tree.postorder()]
