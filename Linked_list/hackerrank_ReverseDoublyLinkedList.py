'''

hackerrank 문제

난이도 : easy

https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

'''

def reverse(head):
    trail = head
    rev = None
    while(head):
        head = head.next
        trail.next = rev
        if rev is not None:
            rev.prev = trail
        rev = trail
        trail = head
    return rev
