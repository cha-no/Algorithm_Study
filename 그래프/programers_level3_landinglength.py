
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3

'''

def solution(dirs):
    answer = 0
    x, y = 0, 0
    dirs_dict = {"U":(0, 1), "R":(1, 0), "D":(0, -1), "L":(-1, 0)}
    rev_dict = {"U":"D", "R":"L", "D":"U", "L":"R"}
    visit = {}
    
    for d in dirs:
        dx, dy = dirs_dict[d]
        if x+dx < -5 or x+dx>5 or y+dy < -5 or y+dy>5:
            continue
        if visit.get((x,y),0):
            if d not in visit[(x,y)]:
                visit[(x,y)].append(d)
                answer += 1
        else:
            visit[(x,y)] = [d]
            answer += 1
        x+=dx
        y+=dy
        visit[(x,y)] = visit.get((x,y),[])
        visit[(x,y)].append(rev_dict[d])

    return answer
