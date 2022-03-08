"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the
    cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""
from collections import OrderedDict


class LRUCache:
    """
    Original idea of using deque + dict is too slow, any updating of existing order in queue would be O(n)
    Dict preserves insertion order from 3.6+ but would be too slow (O(n) to access "last" element (cast to list))

    OrderedDict (and deque) are implemented as double-linked lists internally so this is simpler but equivalent
    to the "full" linked list implementation detailed below.
    """
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # cache hits pushed to rear (could also delete/append)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)  # FIFO last=True, LIFO last=False
        else:
            self.cache.move_to_end(key)  # new insertions go to rear (could also delete/append)
            self.cache[key] = value


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCacheLL:
    """
    Linked list where nodes are stored/accessed via dict
    """

    def __init__(self, capacity: int):
        self.dic = dict()  # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:  # similar to get()
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value  # replace the value len(dic)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key, value)
            self.dic[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def removeFromTail(self):
        if len(self.dic) == 0:
            return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)


# TODO: test code
"""
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
"""



