#642. Moving Average from Data Stream

<滚动数组>

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.id = 0
        self.Sum = [0]*(size + 1)
        

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        def mod(x):
            return x % (self.size+1)
        self.id += 1
        self.Sum[mod(self.id)] = self.Sum[mod(self.id-1)] + val
        if (self.id - self.size) >= 0:
            return (self.Sum[mod(self.id)] - self.Sum[mod(self.id- self.size)]) / self.size
        else:
            return (self.Sum[mod(self.id)] / self.id)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)

'''
笔记:
两种方法节省空间复杂度：
	1. 链表
	2. 滚动数组
'''
<leetcode 老版本>
import collections

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)