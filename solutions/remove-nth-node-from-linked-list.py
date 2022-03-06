"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Tests:
    @staticmethod
    def create_llinked_list_from_flat_list(value_list):
        dummy = current = ListNode()
        for i, val in enumerate(value_list):
            current.val = val
            if i < (len(value_list)-1):
                current.next = ListNode(value_list[i+1])
            current = current.next
        return dummy


class Solution:
    @staticmethod
    def removeNthFromEnd(head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


# test code
e1 = Tests.create_llinked_list_from_flat_list([1, 2, 3, 4, 5])
e2 = Tests.create_llinked_list_from_flat_list([1])
e3 = Tests.create_llinked_list_from_flat_list([1, 2])

assert Solution.removeNthFromEnd(e1, 2).next.next.next.val == 5
assert Solution.removeNthFromEnd(e2, 1) is None
assert Solution.removeNthFromEnd(e3, 1).val == 1

