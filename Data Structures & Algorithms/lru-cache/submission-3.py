from collections import deque

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertNode(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            nodeToRemove = self.cache[key]
            self.removeNode(nodeToRemove) # remove from pos. in LL
            self.insertNode(nodeToRemove) # add to end of LL (MRU pos.)
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key] # finds node in LL
            self.removeNode(node) # removes node from LL
            self.insertNode(node) # adds node to far right (MRU)
            self.cache[key].val = value # updates cache
        else:
            isCacheFull = len(self.cache) == self.capacity
            nodeToAdd = Node(key, value)
            if isCacheFull:
                self.cache.pop(self.left.next.key)
                self.removeNode(self.left.next)
            
            self.cache[key] = nodeToAdd
            self.insertNode(nodeToAdd)

        


        
