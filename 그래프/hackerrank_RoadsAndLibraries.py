'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

'''

def roadsAndLibraries(n, c_lib, c_road, cities):
    def dfs(arr,visit,s):
        visit[s] = 1
        v = 0
        for i in arr[s]:
            if not visit[i]:
                v += 1
                v += dfs(arr,visit,i)
        return v
    if c_lib < c_road:
        return n * c_lib
    if not len(cities):
        return n * c_lib
    arr = [[0] for i in range(n)]
    visit = [0 for i in range(n)]
    for i in range(n):
        arr[i][0] = i
    for i in cities:
        arr[i[0]-1].append(i[1]-1)
        arr[i[1]-1].append(i[0]-1)
    v = 0
    for i in range(n):
        if not visit[i]:
            v += dfs(arr,visit,i)
    return ((n-v)*c_lib + v*c_road)
