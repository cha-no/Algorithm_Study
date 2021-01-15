
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/42893

'''
import re

def solution(word, pages):
    link_dict = {}
    index_dict = {}
    basic_dict = {}
    score_dict = {}

    for i in range(len(pages)):
        page = re.search('<head>.+<meta property="og:url" content=["](\S+)["].+</head>',pages[i],re.DOTALL).group(1)
        index_dict[page] = i

        links = re.findall('<a href="(.+?)"', pages[i], re.DOTALL)
        for link in links:
            link_dict[link] = link_dict.get(link,[])
            link_dict[link].append(page)

        basic_score = re.sub('[^a-zA-Z]', ' ', pages[i]).lower().split().count(word.lower())
        basic_dict[index_dict[page]] = basic_dict.get(index_dict[page], [])
        basic_dict[index_dict[page]].append(basic_score)
        basic_dict[index_dict[page]].append(len(links))

    for page in index_dict:
        links = link_dict.get(page, [])
        link_score = 0
        if links:
            for link in links:
                link_score += (basic_dict[index_dict[link]][0]/basic_dict[index_dict[link]][1])
        score_dict[index_dict[page]] = link_score + basic_dict[index_dict[page]][0]

    return sorted(score_dict.items(), key = lambda x: (-x[1], x[0]))[0][0]
