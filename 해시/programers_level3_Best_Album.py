
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

'''

from typing import List

def solution(genres : List[str], plays : List[int]) -> List[int]:
    answer = []
    play_dict = {}
    genre_dict = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        play_dict[genre] = play_dict.get(genre, 0) + play
        genre_dict[genre] = genre_dict.get(genre, [])
        genre_dict[genre].append((play, i))
    
    play_sort = sorted(play_dict.items(), key = lambda x : x[1], reverse = True)
    
    for (genre, _) in play_sort:
        genre_dict[genre] = sorted(genre_dict[genre], key = lambda x : x[0], reverse = True)
        answer += list(list(zip(*genre_dict[genre][:2]))[1])
    
    return answer
