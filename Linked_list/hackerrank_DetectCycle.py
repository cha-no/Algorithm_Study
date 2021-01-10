'''

hackerrank 문제

난이도 : easy

https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

'''

def has_cycle(head):
    data_set = set()
    while(head):
        if head.data in data_set:
            return True
        data_set.add(head.data)
        head = head.next
