"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeTwoLists(l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


# test code
l1_2 = ListNode(4)
l1_1 = ListNode(2, next=l1_2)
l1_0 = ListNode(1, next=l1_1)

l2_2 = ListNode(4)
l2_1 = ListNode(3, next=l2_2)
l2_0 = ListNode(1, next=l2_1)

l_zero = ListNode(0)

assert Solution.mergeTwoLists(l1_0, l2_0).next.next.next.next.next.val == 4
assert Solution.mergeTwoLists(None, None) is None
assert Solution.mergeTwoLists(None, l_zero).val == 0
