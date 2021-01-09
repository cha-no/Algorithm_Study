
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3

'''


def solution(n, costs):
    def find(u):
        return u if visit[u] < 0 else find(visit[u])
    answer = 0
    visit = [-1]*n
    costs = sorted(costs, key = lambda x: x[2])
    
    for cost in costs:
        if find(cost[0]) != find(cost[1]):
            visit[find(cost[1])] = find(cost[0])
            answer += cost[2]
        if visit.count(-1)==1:
            break
    return answer
