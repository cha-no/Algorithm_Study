
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/49191

'''

def solution(n, results):
    answer = 0
    graph = [[0]*n for i in range(n)]
    
    for result in results:
        graph[result[0]-1][result[1]-1] = 1
        graph[result[1]-1][result[0]-1] = -1
        stack = [(result[0]-1, result[1]-1)]
        while stack:
            w, l = stack.pop()
            for i in range(n):
                if not graph[l][i]:
                    if graph[w][i] == -1:
                        graph[l][i] = -1
                        graph[i][l] = 1
                        stack.append((i,l))
                if not graph[w][i]:
                    if graph[l][i] == 1:
                        graph[w][i] = 1
                        graph[i][w] = -1
                        stack.append((w,i))
                
    for i in range(n):
        if graph[i].count(0)==1:
            answer += 1
        
    return answer
