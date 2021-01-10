'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/min-max-riddle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

'''

def riddle(arr, n):
    answer = []
    stack = []
    a_dict = {}
    arr.append(0)
    for i in range(n+1):
        t = i
        while stack and arr[stack[-1][0]] > arr[i]:
            l, lt = stack.pop()
            if arr[l] in a_dict:
                a_dict[arr[l]] = max(a_dict[arr[l]],i-lt)
            else:
                a_dict[arr[l]] = i-lt
            if arr[i] in a_dict:
                a_dict[arr[i]] = max(a_dict[arr[i]],i-lt+1)
            else:
                a_dict[arr[i]] = i-lt+1
            t = lt
        stack.append((i,t))
    a_dict.pop(0)
    a_l = sorted(a_dict.items(), key = lambda x: (x[1],x[0]))
    for i in range(n, 0, -1):
        if not answer:
            answer.append(a_l.pop()[0])
            continue
        if a_l[-1][1] == i:
            if answer[-1] > a_l[-1][0]:
                answer.append(answer[-1])
            else:
                answer.append(a_l[-1][0])
            while a_l and a_l[-1][1] >= i:
                a_l.pop()
        else:
            answer.append(answer[-1])
    
    answer.reverse()
    return answer
