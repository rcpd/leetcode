"""
Copy-pasta for leetcode style linked list generation
"""


class ListNode(object):
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


# test code
test_data = [[1, 4, 5], [1, 3, 4], [2, 6]]

for i, llist_val in enumerate(test_data):
    test_data[i] = Tests.create_llinked_list_from_flat_list(llist_val)

    # dump list
    current = test_data[i]
    while current:
        print(current.val)
        current = current.next

assert test_data[0].next.next.val == 5
assert test_data[1].next.next.val == 4
assert test_data[2].next.val == 6

