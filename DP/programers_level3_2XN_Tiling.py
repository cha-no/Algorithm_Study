
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

'''

import heapq

class DoubleHeap(object):
    
    def __init__(self) -> None:
        self.__max_heap = []
        self.__min_heap = []
        self.__number = 0
    
    def push(self, num : int) -> None:
        heapq.heappush(self.__max_heap, -num)
        heapq.heappush(self.__min_heap, num)
        self.__number += 1

    def popMax(self) -> int:
        item = None
        if self.__max_heap:
            item = -heapq.heappop(self.__max_heap)
            self.__number -= 1
        if not self.__max_heap or not self.__number:
            self.__max_heap = []
            self.__min_heap = []
        return item
        
    def popMin(self) -> int:
        item = None
        if self.__min_heap:
            item = heapq.heappop(self.__min_heap)
            self.__number -= 1
        if not self.__min_heap or not self.__number:
            self.__max_heap = []
            self.__min_heap = []
        return item
    
    def getMax(self) -> int:
        item = 0
        if self.__max_heap:
            item = -self.__max_heap[0]
        return item

    def getMin(self) -> int:
        item = 0
        if self.__min_heap:
            item = self.__min_heap[0]
        return item

def solution(operations):
    doubleheap = DoubleHeap()
    for operation in operations:
        oper, num = operation.split()
        if oper == 'I':
            doubleheap.push(int(num))
        else:
            if num == '1':
                doubleheap.popMax()
            else:
                doubleheap.popMin()
    return [doubleheap.getMax(), doubleheap.getMin()]
