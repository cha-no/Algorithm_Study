'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

'''

def decodeHuff(root, s):
    #Enter Your Code Here
    answer = ''
    temp = root
    for i in s:
        if i == '1':
            temp = temp.right
        else:
            temp = temp.left
        if temp.data != '\0':
            answer += temp.data
            temp = root
    print(answer)
