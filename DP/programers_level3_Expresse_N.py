
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3

'''

from collections import defaultdict

def solution(N, number):
    dp_dict = defaultdict(set)
    answer = 1
    
    while answer <= 8:
        for i in range(1, 1 + answer//2):
            j = answer - i
            for ele1 in dp_dict[i]:
                for ele2 in dp_dict[j]:
                    dp_dict[answer].add(ele1 + ele2)
                    dp_dict[answer].add(ele1 - ele2)
                    dp_dict[answer].add(ele2 - ele1)
                    dp_dict[answer].add(ele1 * ele2)
                    if ele2:
                        dp_dict[answer].add(ele1 // ele2)
                    if ele1:
                        dp_dict[answer].add(ele2 // ele1)
        dp_dict[answer].add((10**answer - 1)*N//9)
        
        for ele in dp_dict[answer]:
            if ele == number:
                break
        else:
            answer += 1
            continue
        break
    else:
        answer = -1
    return answer
