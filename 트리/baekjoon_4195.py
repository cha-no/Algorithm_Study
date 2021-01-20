'''

백준 문제

https://www.acmicpc.net/problem/4195

'''

def find(v):
    return v if isinstance(network[v], int) and network[v]<0 else find(network[v])

if __name__ == "__main__":
    t = int(input())
    
    for i in range(t):
        f = int(input())
        network = {}

        for i in range(f):
            f1, f2 = input().split()
            network[f1] = network.get(f1, -1)
            network[f2] = network.get(f2, -1)
            
            if find(f1) != find(f2):
                if network[find(f1)] < network[find(f2)]:
                    network[find(f1)] += network[find(f2)]
                    network[find(f2)] = find(f1)
                else:
                    network[find(f2)] += network[find(f1)]
                    network[find(f1)] = find(f2)

            print(-network[find(f1)])
