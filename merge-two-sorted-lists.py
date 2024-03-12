"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = cur = ListNode()
        # walk both lists
        while list1 and list2:
            # lower of 2 vals appends onto new list and is advanced
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            # current node advances in either case
            cur = cur.next

        # append remaining (logger) list onto new list
        cur.next = list1 or list2
        return dummy.next  # return head of new list excluding dummy


# test code
l1_2 = ListNode(4)
l1_1 = ListNode(2, next=l1_2)
l1_0 = ListNode(1, next=l1_1)

l2_2 = ListNode(4)
l2_1 = ListNode(3, next=l2_2)
l2_0 = ListNode(1, next=l2_1)

l_null = ListNode(-101)
l_zero = ListNode(0)

assert Solution.mergeTwoLists(l1_0, l2_0) == ListNode()
assert Solution.mergeTwoLists(l_null, l_null) == l_null
assert Solution.mergeTwoLists(l_null, l_zero) == l_zero
