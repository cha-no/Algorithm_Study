
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

'''

def solution(begin, target, words):
    def isPossible(word1, word2):
        return sum([1 if word1[i] == word2[i] else 0 for i in range(len(word1))]) == len(word1) - 1
    
    n = len(words)
    answer = 0
    visit = [0] * n
    graph = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i):
            if isPossible(words[i], words[j]):
                graph[i][j] = 1
                graph[j][i] = 1
    
    queue = []
    for i in range(n):
        if isPossible(begin, words[i]):
            queue.append((i, 1))
            visit[i] = 1
    print(queue)
    while queue:
        (i, count), queue = queue[0], queue[1:]
        if words[i] == target:
            answer = count
            break
        
        for j in range(n):
            if visit[j] or not graph[i][j]:
                continue            
            queue.append((j, count + 1))
            visit[j] = 1
    return answer
