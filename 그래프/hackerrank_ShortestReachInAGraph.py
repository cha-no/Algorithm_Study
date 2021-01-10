'''

hackerrank 문제

난이도 : hard

https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

'''

class Graph(object):
    def __init__(self, n):
        self.n = n
        self.g = [[0]*n for i in range(n)]
    
    def connect(self,x,y):
        self.g[x][y] = 1
        self.g[y][x] = 1
    
    def find_all_distances(self, s):
        dist = [-1]*self.n
        visit = [0]*self.n
        
        visit[s] = 1
        queue = [s]
        while queue:
            node, queue = queue[0], queue[1:]
            d = 6 * visit[node]
            for i in range(self.n):
                if self.g[node][i] and not visit[i]:
                    queue.append(i)
                    dist[i] = d
                    visit[i] = visit[node]+1
        dist.pop(s)
        print(" ".join(list(map(str, dist))))
