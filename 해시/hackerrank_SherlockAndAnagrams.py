'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

'''

def sherlockAndAnagrams(s):
    answer = 0
    n = len(s)
    for i in range(1, n+1):
        s_dict = {}
        for j in range(n-i+1):
            temp = ''.join(sorted(s[j:j+i]))
            s_dict[temp] = s_dict.get(temp,0)+1
        for k in s_dict:
            if s_dict[k] > 1:
                answer += (s_dict[k]*(s_dict[k]-1))//2
    return answer
