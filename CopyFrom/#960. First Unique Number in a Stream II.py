#960. First Unique Number in a Stream II

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}
        
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num not in self.dict:
            node = Node(num)
            self.dict[num] = node
            prev = self.tail.prev
            next = self.tail
            prev.next = node
            node.prev = prev
            next.prev = node
            node.next = next
        else:
            if self.dict[num]:
                node = self.dict[num]
                self.dict[num] = None
                prev = node.prev
                next = node.next
                next.prev = prev
                prev.next = next
        
    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        return self.head.next.val