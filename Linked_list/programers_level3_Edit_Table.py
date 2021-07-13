
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/81303?language=python3

'''


from typing import List

class Node(object):
    def __init__(self, item : int) -> None:
        self.__item = item
        self.__left = None
        self.__right = None
    
    @property
    def item(self) -> int:
        return self.__item
    
    @item.setter
    def item(self, item : int) -> None:
        self.__item = item

    @property
    def left(self) -> int:
        return self.__left
    
    @left.setter
    def left(self, item : int) -> None:
        self.__left = item

    @property
    def right(self) -> int:
        return self.__right
    
    @right.setter
    def right(self, item : int) -> None:
        self.__right = item

class DoubleLinkedList(object):
    def __init__(self, n : int, k : int) -> None:
        self.__n = n
        self.__k = k
        self.__list = [0] * n
        self.__state = [1] * n
        self.__stack = []
        for i in range(n):
            node = Node(i)
            node.left = i - 1
            node.right = i + 1
            if not i:
                node.left = n - 1
            if i == n - 1:
                node.right = 0
            self.__list[i] = node
    
    def operate(self, command : str) -> None:
        if command[0] == 'U':
            oper, count = command.split()
            count = int(count)
            while count:
                self.__k = self.__list[self.__k].left
                count -= 1
        elif command[0] == 'D':
            oper, count = command.split()
            count = int(count)
            while count:
                self.__k = self.__list[self.__k].right
                count -= 1
        elif command[0] == 'C':
            self.__list[self.__list[self.__k].right].left = self.__list[self.__k].left
            self.__list[self.__list[self.__k].left].right = self.__list[self.__k].right
            self.__stack.append(self.__k)
            self.__state[self.__k] = 0
            if self.__list[self.__k].right:
                self.__k = self.__list[self.__k].right
            else:
                self.__k = self.__list[self.__k].left                
        else:
            k = self.__stack.pop()
            self.__state[k] = 1            
            self.__list[self.__list[k].left].right = k
            self.__list[self.__list[k].right].left = k
    
    def get_answer(self) -> str:
        answer = ''
        for i in range(self.__n):
            if not self.__state[i]:
                answer += 'X'
            else:
                answer += 'O'
        return answer
    
def solution(n : int, k : int, cmd : List[str]) -> str:
    double_linked_list = DoubleLinkedList(n, k)
    for command in cmd:
        double_linked_list.operate(command)
    return double_linked_list.get_answer()
