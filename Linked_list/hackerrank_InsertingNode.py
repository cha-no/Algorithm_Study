'''

hackerrank 문제

난이도 : easy

https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

'''

def sortedInsert(head, data):
    d_node = DoublyLinkedListNode(data)
    if head is None:
        head = d_node
        return head
    temp = head
    while head:
        print(head.data)
        if head.next:
            if head.data <= data and head.next.data >= data:
                d_node.next = head.next
                head.next = d_node
                break
            elif head.prev is None and head.data >= data:
                d_node.next = head
                temp = d_node
                break
        else:
            if head.data <= data:
                d_node.next = head.next
                head.next = d_node
                break
        head = head.next
    return temp
