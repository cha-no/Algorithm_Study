'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/minimum-time-required/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

'''

def minTime(machines, goal):
    answer = 0
    s = int(goal // (len(machines)/min(machines)))
    e = int(goal // (len(machines)/max(machines))) + 1
    while(s<=e):
        make = 0
        m = (s+e)//2
        for machine in machines:
            make += m//machine
        if goal > make:
            s = m + 1
            continue
        else:
            answer = m
            e = m - 1
    return answer
