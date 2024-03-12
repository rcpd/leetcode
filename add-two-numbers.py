"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self):
        self.carry = 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []

        # walk both lists
        while l1 or l2:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            # same as long form addition
            num = val1 + val2
            if self.carry:
                num += self.carry
                self.carry = 0

            if num >= 10:
                self.carry += 1
                num -= 10

            node = ListNode(val=num, next=None)
            if result:
                result[-1].next = node

            result.append(node)

            # advance list(s)
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

            print(val1, val2, self.carry, "|", num)

        if self.carry:
            print(0, 0, 0, "|", 1)
            node = ListNode(val=self.carry, next=None)
            self.carry = 0
            result[-1].next = node

        return result[0]


# test code
e1_l1_2 = ListNode(val=3, next=None)
e1_l1_1 = ListNode(val=4, next=e1_l1_2)
e1_l1_0 = ListNode(val=2, next=e1_l1_1)
e1_l2_2 = ListNode(val=4, next=None)
e1_l2_1 = ListNode(val=6, next=e1_l2_2)
e1_l2_0 = ListNode(val=5, next=e1_l2_1)

e2_l1_0 = ListNode(val=0, next=None)
e2_l2_0 = ListNode(val=0, next=None)

e3_l1_6 = ListNode(val=9, next=None)
e3_l1_5 = ListNode(val=9, next=e3_l1_6)
e3_l1_4 = ListNode(val=9, next=e3_l1_5)
e3_l1_3 = ListNode(val=9, next=e3_l1_4)
e3_l1_2 = ListNode(val=9, next=e3_l1_3)
e3_l1_1 = ListNode(val=9, next=e3_l1_2)
e3_l1_0 = ListNode(val=9, next=e3_l1_1)
e3_l2_3 = ListNode(val=9, next=None)
e3_l2_2 = ListNode(val=9, next=e3_l2_3)
e3_l2_1 = ListNode(val=9, next=e3_l2_2)
e3_l2_0 = ListNode(val=9, next=e3_l2_1)

# example 1
s = Solution()
s.addTwoNumbers(e1_l1_0, e1_l2_0)
print("Solution: [7,0,8]\n")
s.addTwoNumbers(e2_l1_0, e2_l2_0)
print("Solution: [0]\n")
s.addTwoNumbers(e3_l1_0, e3_l2_0)
print("Solution: [8,9,9,9,0,0,0,1] \n")


