'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

'''

def triplets(a, b, c):
    a.sort(), b.sort(), c.sort()
    lena, lenb, lenc = len(a), len(b), len(c)
    answer = 0
    ca, cc = 0, 0
    ia, ic = 0, 0
    tempa, tempb, tempc = 0, 0, 0
    for i in range(lenb):
        if tempb==b[i]:
            continue
        tempb = b[i]
        while ia < lena and a[ia]<=tempb:
            if tempa==a[ia]:
                ia += 1
                continue
            tempa = a[ia]
            ca += 1
            ia += 1
        while ic < lenc and c[ic]<=tempb:
            if tempc==c[ic]:
                ic += 1
                continue
            tempc = c[ic]
            cc += 1
            ic += 1
        
        answer += ca*cc
    return answer
