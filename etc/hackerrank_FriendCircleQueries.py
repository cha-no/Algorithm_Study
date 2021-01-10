'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/friend-circle-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous

'''

def maxCircle(queries):
    def find(x):
        if parent_dict[x] < 0:
            return x, parent_dict[x]
        x = parent_dict[x]
        return find(x)
    answer = []
    parent_dict = {}
    temp = 0
    for query in queries:
        if query[0] not in parent_dict:
            parent_dict[query[0]] = -1
        if query[1] not in parent_dict:
            parent_dict[query[1]] = -1
        c1, p1 = find(query[0])
        c2, p2 = find(query[1])
        if c1 != c2:
            if p1 < p2:
                parent_dict[c1] = p1+p2
                parent_dict[c2] = c1                
            else:
                parent_dict[c2] = p1+p2
                parent_dict[c1] = c2
        temp = min(temp,min(parent_dict[c1],parent_dict[c2]))
        answer.append(-temp)
    return answer
