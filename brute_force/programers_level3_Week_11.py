
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/87694?language=python3

'''


from typing import List

def makeShape(rectangle : List[List[int]]) -> List[List[int]] :
    graph = [[0] * 101 for i in range(101)]
    
    for (x1, y1, x2, y2) in rectangle :
        for x in range(2*x1, 2*x2 + 1) :
            for y in range(2*y1, 2*y2 + 1) :
                if (x == 2*x1 or x == 2*x2 or y == 2*y1 or y == 2*y2) :
                    if not graph[x][y] :
                        graph[x][y] = -1
                else :
                    if graph[x][y] == -1 : graph[x][y] = 0
                    graph[x][y] += 1
    return graph

def isPossible(x : int, y : int, curDir : int, graph : List[List[int]]) -> bool :
    if not (1 <= x <= 100 and 1 <= y <= 100) : return False
    if curDir == 0 :
        if (graph[x][y] == -1 and graph[x - 1][y] == -1) : return True
    elif curDir == 1 :
        if (graph[x][y] == -1 and graph[x + 1][y] == -1) : return True
    elif curDir == 2 :
        if (graph[x][y] == -1 and graph[x][y - 1] == -1) : return True
    else :
        if (graph[x][y] == -1 and graph[x][y + 1]) : return True
    return False

def getPosses(characterX : int, characterY : int, graph : List[List[int]]) -> List[int] :
    posses = []
    for d in range(4) :
        if d == 0 : tempX, tempY = 2*characterX + 2, 2*characterY
        elif d == 1 : tempX, tempY = 2*characterX - 2, 2*characterY
        elif d == 2 : tempX, tempY = 2*characterX, 2*characterY + 2
        else : tempX, tempY = 2*characterX, 2*characterY - 2
        if isPossible(tempX, tempY, d, graph) : posses.append(d)
    return posses

def getDistance(characterX : int, characterY : int, itemX : int, itemY : int, startDir : int, graph : List[List[int]]) -> int :
    distance = 1
    characterX *= 2
    characterY *= 2
    curDir = startDir
    dx = [2, -2, 0, 0]
    dy = [0, 0, 2, -2]
    if startDir == 0 : characterX += 2
    elif startDir == 1 : characterX -= 2
    elif startDir == 2 : characterY += 2
    else : characterY -= 2
    
    while not (characterX == 2 * itemX and characterY == 2 * itemY) :
        for i in range(4) :
            if i == 0 and curDir == 1 : continue               
            elif i == 1 and curDir == 0 : continue
            elif i == 2 and curDir == 3 : continue
            elif i == 3 and curDir == 2 : continue
            tempX, tempY = characterX + dx[i], characterY + dy[i]
            if isPossible(tempX, tempY, i, graph) :
                characterX, characterY = tempX, tempY
                curDir = i
                distance += 1
                break

    return distance

def solution(rectangle : List[List[int]], characterX : int, characterY : int, itemX : int, itemY : int) -> int :
    answer = 2 * 50 ** 2 + 1
    
    graph = makeShape(rectangle)
    posses = getPosses(characterX, characterY, graph)
            
    for startDir in posses :
        answer = min(answer, getDistance(characterX, characterY, itemX, itemY, startDir, graph))
    return answer
