
'''

프로그래머스 level4 문제

https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3

'''



from typing import List, Any
import sys
sys.setrecursionlimit(100000)

class Trie(object):
    def __init__(self) -> None:
        self.__children = [0] * 26
        self.__level = 0
        self.__child = 0
                    
    def insert(self, word : str) -> None:
        level = 1
        node = self
        for s in word:
            index = char_to_index(s)
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
            node.child += 1
            node.level = level
            level += 1
            
    def find(self, word : str) -> int:
        count = 0
        node = self
        for s in word:
            index = char_to_index(s)
            node = node.children[index]
            if node.child == 1:
                count = node.level
                break
            
        return count if count else len(word)
    
    @property
    def children(self) -> List[Any]:
        return self.__children

    @property
    def level(self) -> int:
        return self.__level
    
    @level.setter
    def level(self, level : int) -> None:
        self.__level = level

    @property
    def child(self) -> int:
        return self.__child
    
    @child.setter
    def child(self, child : int) -> None:
        self.__child = child

def char_to_index(char : str) -> int:
    return ord(char) - ord('a')

def solution(words : List[str]) -> int:
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    for word in words:
        answer += trie.find(word)
    return answer
