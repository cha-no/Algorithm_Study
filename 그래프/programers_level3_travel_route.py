
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3#

'''

def solution(tickets):
    def airport_path(tickets, answer, visit, index):
        visit[index] = 1
        airport = tickets[index][1]
        answer.append(airport)
        for i, (air1, air2) in enumerate(tickets):
            if visit[i]:
                continue
            if air1 == airport:
                answer = airport_path(tickets, answer, visit, i)
        if 0 in visit:
            answer.pop()
            visit[index] = 0
        return answer
        
    tickets = sorted(tickets)
    for index, (air1, air2) in enumerate(tickets):
        if air1 == 'ICN':
            answer = ['ICN']
            visit = [0] * len(tickets)
            answer = airport_path(tickets, answer, visit, index)
            if not 0 in visit:
                break
            
    return answer
