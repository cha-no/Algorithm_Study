
'''

프로그래머스 level3 문제

https://school.programmers.co.kr/learn/courses/30/lessons/131129

'''



from typing import List

def solution(scores: List[List[int]]) -> int:
    wanho_atti, wanho_peer = scores[0]
    wanho_score = wanho_atti + wanho_peer
    wanho_large_score = sorted([scores[i] for i in range(1, len(scores)) if sum(scores[i]) > wanho_score], key=lambda x: (-x[0], x[1]))

    not_incentive_cnt = 0
    prev_max_atti = -1
    prev_atti = -1
    prev_max_peer = -1
    prev_group_max_peer = -1
    for atti, peer in wanho_large_score:
        if atti > wanho_atti and peer > wanho_peer:
            return -1
        if prev_max_peer == -1 and prev_max_atti == -1:
            prev_max_atti = atti
            prev_atti = atti
            prev_max_peer = peer
            prev_group_max_peer = peer
            continue
        if atti != prev_atti:
            prev_max_peer = max(prev_max_peer, prev_group_max_peer)
        if prev_max_atti > atti and prev_max_peer > peer:
            not_incentive_cnt += 1
        prev_group_max_peer = max(prev_group_max_peer, peer)
        prev_atti = atti
    return len(wanho_large_score) - not_incentive_cnt + 1
