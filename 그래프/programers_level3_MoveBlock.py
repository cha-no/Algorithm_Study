
'''

프로그래머스 level3 문제

https://programmers.co.kr/learn/courses/30/lessons/60063?language=python3#

'''
def solution(board):
    def move_right(x, y, d):
        return x, y + 1, d
    def move_left(x, y, d):
        return x, y - 1, d
    def move_up(x, y, d):
        return x - 1, y, d
    def move_down(x, y, d):
        return x + 1, y, d
    def move_benefit(x, y, d):
        return (x, y + 1, d^1) if d else (x + 1, y, d^1)
    def move_loss(x, y, d):
        return (x - 1, y, d^1) if d else (x, y - 1, d^1)
    def move_sustain1(x, y, d):
        return (x - 1, y + 1, d^1) if d else (x, y, d^1)
    def move_sustain2(x, y, d):
        return (x, y, d^1) if d else (x + 1, y - 1, d^1)
    def isWall(x, y, d):
        return (board[x][y] or board[x-1][y]) if d else (board[x][y] or board[x][y-1])
    def isEnd(x, y, N = len(board)):
        return x == N-1 and y == N-1
    def getPossible(x, y, d, N = len(board)):
        possible = []
        
        for (m, f) in move_dict.items():
            if m == 'right':
                m_x, m_y, m_d = f(x, y, d)
                if m_y >= N or isWall(m_x, m_y, m_d):
                    continue
                possible.append((m_x, m_y, m_d))
            elif m == 'left':
                m_x, m_y, m_d = f(x, y, d)
                if m_y - (d^1) < 0 or isWall(m_x, m_y, m_d):
                    continue
                possible.append((m_x, m_y, m_d))
            elif m == 'up':
                m_x, m_y, m_d = f(x, y, d)
                if m_x - d < 0 or isWall(m_x, m_y, m_d):
                    continue
                possible.append((m_x, m_y, m_d))
            elif m == 'down':
                m_x, m_y, m_d = f(x, y, d)
                if m_x >= N or isWall(m_x, m_y, m_d):
                    continue
                possible.append((m_x, m_y, m_d))
            elif m == 'benefit':
                m_x, m_y, m_d = f(x, y, d)
                if d and (m_y >= N or board[x-1][y+1]):
                    continue
                elif not d and (m_x >= N or board[x+1][y-1]):
                    continue
                if isWall(m_x, m_y, m_d):
                    continue
                possible.append((m_x, m_y, m_d))
            elif m == 'loss':
                m_x, m_y, m_d = f(x, y, d)
                if d and (m_y - 1 < 0 or board[x][y-1]):
                    continue
                elif not d and (m_x - 1 < 0 or board[x-1][y]):
                    continue
                if isWall(m_x, m_y, m_d):
                    continue
                possible.append((m_x, m_y, m_d))
            elif m == 'sustain1':
                m_x, m_y, m_d = f(x, y, d)
                if d and (m_y >= N or board[x][y+1]):
                    continue
                elif not d and (m_x - 1 < 0 or board[x-1][y-1]):
                    continue
                if isWall(m_x, m_y, m_d):
                    continue
                possible.append((m_x, m_y, m_d))
            else:
                m_x, m_y, m_d = f(x, y, d)
                if d and (m_y - 1 < 0 or board[x-1][y-1]):
                    continue
                elif not d and (m_x >= N or board[x+1][y]):
                    continue
                if isWall(m_x, m_y, m_d):
                    continue
                possible.append((m_x, m_y, m_d))
        return possible
    
    N = len(board)
    start = 0, 1
    d = 0
    cost = 0
    move_dict = {'right':move_right, 'left':move_left, 'up':move_up, 'down':move_down, 'benefit':move_benefit, 'loss':move_loss, 'sustain1':move_sustain1, 'sustain2':move_sustain2}
    visit = set()
    visit.add((start[0], start[1], d))
    
    queue = [(start[0], start[1], d, cost)]
    while queue:
        (x, y, d, cost), queue = queue[0], queue[1:]
        if isEnd(x, y, N):
            answer = cost
            break
        
        for (m_x, m_y, m_d) in getPossible(x, y, d):
            if (m_x, m_y, m_d) in visit:
                continue
            visit.add((m_x, m_y, m_d))
            queue.append((m_x, m_y, m_d, cost + 1))

    return answer
