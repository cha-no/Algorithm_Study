'''

hackerrank 문제

난이도 : medium

https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

'''

class MyQueue(object):
    def __init__(self):
        self.array = []
    
    def peek(self):
        return self.array[0]
        
    def pop(self):
        self.array.pop(0)
        
    def put(self, value):
        self.array.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
