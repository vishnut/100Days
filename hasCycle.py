"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    slow = head
    fast = head
    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next
        if fast == None:
            return False
        fast = fast.next
        if slow == fast:
            return True
    return False