
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/87391?language=python3

'''


class Square(object) :
    def __init__(self, x, y, n, m) :
        self.__l_u = (x, y)
        self.__r_d = (x, y)
        self.__n = n
        self.__m = m
    
    def query(self, command, dx) :
        if command == 0 :
            self.__r_d = (self.__r_d[0], min(self.__r_d[1] + dx, self.__m - 1))
            if self.__l_u[1] != 0 :
                if self.__l_u[1] + dx >= self.__m :
                    self.__l_u, self.__r_d = (-1, -1), (-1, -1)
                self.__l_u = (self.__l_u[0], min(self.__l_u[1] + dx, self.__m - 1))
        elif command == 1 :
            self.__l_u = (self.__l_u[0], max(self.__l_u[1] - dx, 0))
            if self.__r_d[1] != self.__m - 1 :
                if self.__r_d[1] - dx < 0 :
                    self.__l_u, self.__r_d = (-1, -1), (-1, -1)
                self.__r_d = (self.__r_d[0], max(self.__r_d[1] - dx, 0))
        elif command == 2 :
            self.__r_d = (min(self.__r_d[0] + dx, self.__n - 1), self.__r_d[1])
            if self.__l_u[0] != 0 :
                if self.__l_u[0] + dx >= self.__n :
                    self.__l_u, self.__r_d = (-1, -1), (-1, -1)
                self.__l_u = (min(self.__l_u[0] + dx, self.__n - 1), self.__l_u[1])
        else :
            self.__l_u = (max(self.__l_u[0] - dx, 0), self.__l_u[1])
            if self.__r_d[0] != self.__n - 1 :
                if self.__r_d[0] - dx < 0 :
                    self.__l_u, self.__r_d = (-1, -1), (-1, -1)
                self.__r_d = (max(self.__r_d[0] - dx, 0), self.__r_d[1])
    
    def isPossible(self) :
        return self.__l_u[0] == -1
    
    def getAnswer(self) :
        return (self.__r_d[0] - self.__l_u[0] + 1) * (self.__r_d[1] - self.__l_u[1] + 1)

def solution(n, m, x, y, queries):
    square = Square(x, y, n, m)
    
    for (command, dx) in reversed(queries) :
        square.query(command, dx)
        if square.isPossible() : return 0
    
    return square.getAnswer()
