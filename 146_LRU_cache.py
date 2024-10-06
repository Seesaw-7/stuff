from collections import deque

# Use queue, dict and another dict that counts 
class LRUCache1:

    def __init__(self, capacity: int):
        self.seq = deque()
        self.data = {}
        self.occurance = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.data:
            self.seq.append(key)
            self.occurance[key] += 1
        return self.data.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.occurance[key] += 1
        else:
            if self.capacity == 0:
                k = self.seq.popleft()
                while self.occurance[k] > 1:
                    self.occurance[k] -= 1
                    k = self.seq.popleft()
                self.occurance.pop(k)
                self.data.pop(k)
            else:
                self.capacity -= 1
            self.occurance[key] = 1
        self.data[key] = value
        self.seq.append(key)

# doubly linked list and dict     
class Node():
    def __init__(self, key =0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.key2node = {}

    def get(self, key: int) -> int:
        if key in self.key2node:
            node = self.key2node[key]

            #remove the node from list
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.head
            node.next = self.head.next

            # insert the node at first
            self.head.next.prev = node
            self.head.next = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            node = self.key2node[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.val = value
        else:
            if self.capacity > 0:
                node = Node(key, value, prev=self.head, next=self.head.next)
                self.head.next.prev = node
                self.head.next = node
                self.key2node[key] = node
                self.capacity -= 1
            else:
                old_key = self.tail.prev.key
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
                self.key2node.pop(old_key)
                node = Node(key, value, prev=self.head, next=self.head.next)
                self.head.next.prev = node
                self.head.next = node
                self.key2node[key] = node

# Using Python dict, which is ordered according to the insertion order (Python3.7)        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2val = {}

    def get(self, key: int) -> int:
        if key in self.key2val:
            val = self.key2val.pop(key)
            self.key2val[key] = val
        return self.key2val.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.key2val:
            self.key2val.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
                self.key2val[key] = value
            else:
                self.key2val.pop(next(iter(self.key2val)))
        self.key2val[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)