
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3

'''

def solution(lines):
    def convert(string):
        h, m, s = string.split()[1].split(':')
        during = string.split()[2]
        h = int(h)
        m = int(m)
        s = float(s)
        during = float(during[:-1])
        return h, m, s, during
    
    answer = 0
    start_time = []
    end_time = []
    for line in lines:
        h, m, s, during = convert(line)
        end = 3600*h+60*m+s
        start = end-during+0.001
        start_time.append(start)
        end_time.append(end)
    
    for i in range(len(lines)):
        time1, time2 = start_time[i], end_time[i]
        through1, through2 = 0, 0
        for j in range(len(lines)):
            if start_time[j] <= time1 and time1-1 < end_time[j]:
                through1 += 1
            if start_time[j] <= time2 and time2-1 < end_time[j]:
                through2 += 1
        answer = max(answer, through1, through2)
        
    return answer
