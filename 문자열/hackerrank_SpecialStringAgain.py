'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

'''

def substrCount(n, s):
    s_list = []
    answer = 0
    count = 0
    cur = None
    
    for i in range(n):
        if s[i] == cur:
            count+=1
        else:
            if cur is not None:
                s_list.append((cur, count))
            count = 1
            cur = s[i]
    s_list.append((cur, count))
    
    for i in s_list:
        answer += i[1]*(i[1]+1)//2
    
    for i in range(len(s_list)-2):
        if s_list[i][0]==s_list[i+2][0] and s_list[i+1][1]==1:
            answer += min(s_list[i][1], s_list[i+2][1])
    
    return answer
