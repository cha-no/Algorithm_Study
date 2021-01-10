'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/crossword-puzzle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

'''

def crosswordPuzzle(crossword, words):
    def possWords(crossword, word):
        poss = []
        w_len = len(word)
        for i in range(10):
            for j in range(10-w_len+1):
                if crossword[i][j] != '+':
                    flag = True
                    for k in range(w_len):
                        if not(crossword[i][j+k]==word[k] or crossword[i][j+k]=='-'):
                            flag = False
                            break
                    if flag:
                        if not((j+w_len<10 and crossword[i][j+w_len] not in ['+', 'X']) or (j and crossword[i][j-1] not in ['+', 'X'])):
                            poss.append([i,j,0])

        for i in range(10-w_len+1):
            for j in range(10):
                if crossword[i][j] != '+':
                    flag = True
                    for k in range(w_len):
                        if not(crossword[i+k][j]==word[k] or crossword[i+k][j]=='-'):
                            flag = False
                            break
                    if flag:
                        if not((i+w_len<10 and crossword[i+w_len][j] not in ['+', 'X']) or (i and crossword[i-1][j] not in ['+', 'X'])):
                            poss.append([i,j,1])
        return poss

    def wordPut(crossword, word, indexdirect):
        i, j, d = indexdirect
        if not d:
            for k in range(len(word)):
                crossword[i][j+k] = word[k]
        else:
            for k in range(len(word)):
                crossword[i+k][j] = word[k]

    def backTrack(crossword, word, indexdirect):
        i, j, d = indexdirect
        if not d:
            for k in range(len(word)):
                crossword[i][j+k] = '-'
        else:
            for k in range(len(word)):
                crossword[i+k][j] = '-'

    def isSolve(crossword, words):
        if not len(words):
            for i in range(10):
                print(''.join(crossword[i]))
            return
        
        word = words.pop()
        
        for indexdirect in possWords(crossword, word):
            wordPut(crossword, word, indexdirect)
            isSolve(crossword, words)
            backTrack(crossword, word, indexdirect)
        
        words.append(word)
    
    words = words.split(';')
    
    for i in range(10):
        crossword[i] = list(crossword[i])
    isSolve(crossword, words)

if __name__ == '__main__':

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    crosswordPuzzle(crossword, words)
