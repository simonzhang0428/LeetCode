# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(self, head: ListNode) -> ListNode:
    """
    # >>> lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    # >>> swapPairs(lst, lst)
    # >>> lst
    # ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
    """
    # pre, pre.next = self, head
    # while pre.next and pre.next.next:
    #     a = pre.next
    #     b = a.next
    #     pre.next, b.next, a.next = b, a, b.next
    #     pre = a
    # return self.next

    if not head or not head.next:
        return head
    new_start = head.next.next
    head, head.next = head.next, head
    head.next.next = self.swapPairs(new_start)
    return head


