'''

hackerrank 문제

난이도 : easy

https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

'''

def lca(root, v1, v2):
    #Enter your code here
    if v1 > v2:
        v1, v2 = v2, v1
    
    while(1):
        if v1 <= int(root.info) and int(root.info) <= v2:
            return root
        elif int(root.info) < v1:
            root = (root.right)
        else:
            root = (root.left)
