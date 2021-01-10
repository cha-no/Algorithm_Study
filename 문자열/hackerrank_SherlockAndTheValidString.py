'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

'''

def isValid(s):
    s_dict = {}
    for i in s:
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1
    n_list = list(s_dict.values())
    ma, mi = max(n_list), min(n_list)
    if ma==mi:
        return 'YES'
    if ma-mi==1 and n_list.count(ma) == 1:
        return 'YES'
    if len(set(n_list))==2 and n_list.count(mi) == 1 and mi==1:
        return 'YES'
    return 'NO'
