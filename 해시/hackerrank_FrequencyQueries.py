'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

'''

def freqQuery(queries):
    answer = []
    data_dict = {}
    count_dict = {}
    
    for query in queries:
        if query[0] == 1:
            if query[1] in data_dict:
                count_dict[data_dict[query[1]]] -= 1
                data_dict[query[1]] += 1
                if data_dict[query[1]] in count_dict:
                    count_dict[data_dict[query[1]]] += 1
                else:
                    count_dict[data_dict[query[1]]] = 1
            else:
                data_dict[query[1]] = 1
                if data_dict[query[1]] in count_dict:
                    count_dict[data_dict[query[1]]] += 1
                else:
                    count_dict[data_dict[query[1]]] = 1
        elif query[0] == 2:
            if query[1] in data_dict:
                if data_dict[query[1]] > 1:
                    count_dict[data_dict[query[1]]] -= 1
                    data_dict[query[1]] -= 1
                    if data_dict[query[1]] in count_dict:
                        count_dict[data_dict[query[1]]] += 1
                    else:
                        count_dict[data_dict[query[1]]] = 1
                else:
                    count_dict[data_dict[query[1]]] -= 1
                    data_dict.pop(query[1])
        else:
            if query[1] in count_dict and count_dict[query[1]]:
                answer.append(1)
            else:
                answer.append(0)
    return answer
