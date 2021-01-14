'''

백준 문제

https://www.acmicpc.net/problem/10816

'''

def lowerbound(s,e,value):
    while s<=e:
        m = (s + e)//2
        if nums[m]>=value:
            e = m-1
        else:
            s = m+1
    return s

def upperbound(s,e,value):
    while s<=e:
        m = (s + e)//2
        if nums[m]>value:
            e = m-1
        else:
            s = m+1
    return e

if __name__=="__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    finds = list(map(int, input().split()))

    answer = ''
    nums.sort()

    for find in finds:
        u = upperbound(0,n-1,find)
        l = lowerbound(0,n-1,find)
        answer += str(u-l+1) + ' ' if nums[u]==find and nums[l]==find else '0 '

    print(answer.strip())
