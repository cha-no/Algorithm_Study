'''

hackerrank 문제

난이도 : easy

https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

'''

def luckBalance(k, contests):
    answer = 0
    contests = sorted(contests, key = lambda x: (x[1],-x[0]))
    for contest in contests:
        if contest[1] and k:
            answer += contest[0]
            k-=1
        elif not contest[1]:
            answer += contest[0]
        else:
            answer -= contest[0]
    return answer
