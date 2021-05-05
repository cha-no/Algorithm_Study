
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/77486?language=python3


'''


from typing import List

def solution(enroll : List[str], referral : List[str], seller : List[str], amount : List[int]) -> List[int]:
    def traversal(person : str, money : int) -> None:
        if person != '-':
            if money < 10:
                profit_dict[person] += money
            else:
                profit_dict[person] += money - money // 10
                traversal(parent[person], money // 10)
    
    profit_dict = {name : 0 for name in enroll}
    parent = {c : p for (c, p) in zip(enroll, referral)}
    
    for (person, count) in zip(seller, amount):
        traversal(person, count * 100)
    
    return [profit_dict[person] for person in enroll]
