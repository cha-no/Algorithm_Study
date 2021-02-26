
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/64064

'''

from typing import List, Tuple
from itertools import combinations, permutations

def solution(user_id : List[str], banned_id : List[str]) -> int:
    def isPossible(user : str, ban : str) -> bool:
        if len(user) != len(ban):
            return False
        poss = True
        for (u, b) in zip(user, ban):
            if b != '*' and u != b:
                poss = False
                break
        return poss
    
    def isBan(users : Tuple[str], banned_id : List[str] = banned_id) -> bool:
        for bans in permutations(banned_id, len(banned_id)):
            poss = True
            for (user, ban) in zip(users, bans):
                if not isPossible(user, ban):
                    poss = False
                    break
            else:
                break
        return poss
    
    answer = 0
    for users in combinations(user_id, len(banned_id)):
        answer += 1 if isBan(users, banned_id) else 0
        
    return answer
