'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

'''

def checkBST(node):
    def isBST(node, min_value, max_value):
        if node is None:
            return True
        if node.data <= min_value or node.data >= max_value:
            return False
        return isBST(node.left, min_value, node.data) and isBST(node.right, node.data, max_value)
    return isBST(root, -float('inf'),float('inf'))
