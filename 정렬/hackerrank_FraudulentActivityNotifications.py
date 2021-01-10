'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

'''

def activityNotifications(expenditure, d):
    answer = 0
    ex_dict = {}
    for i in range(len(expenditure)-1):
        if expenditure[i] in ex_dict:
            ex_dict[expenditure[i]] += 1
        else:
            ex_dict[expenditure[i]] = 1
        if i>=d-1:
            if not d%2:
                t = 0
                for j in range(201):
                    if j in ex_dict:
                        t += ex_dict[j]
                    if t >= d//2:
                        break
                t = 0
                for k in range(201):
                    if k in ex_dict:
                        t += ex_dict[k]
                    if t >= d//2+1:
                        break
                med = (j+k)/2
            else:
                t = 0
                for j in range(201):
                    if j in ex_dict:
                        t += ex_dict[j]
                    if t >= d/2:
                        break
                med = j
            if expenditure[i+1] >= 2*med:
                answer += 1
            
            ex_dict[expenditure[i-d+1]]-=1
                
    return answer
