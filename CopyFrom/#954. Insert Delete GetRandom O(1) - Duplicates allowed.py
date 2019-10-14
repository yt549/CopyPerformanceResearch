#954. Insert Delete GetRandom O(1) - Duplicates allowed
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {} # collections.defaultdict(list)
        self.nums = [] 

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        if val in self.map:
            self.map[val].append(len(self.nums) - 1)
            return False
        else:
            self.map[val] = [len(self.nums) - 1].    # HashMap[[list]]; 而且用 “ self.map[val] = list(len(self.nums) - 1) ” 不行
            #  in insert self.map[val] = list(len(self.nums) - 1) TypeError: 'int' object is not iterable； idk WHY
            return True

        '''
        self.nums.append(val)
        self.map.setdefault(val, []).append(len(self.nums) - 1)
        ！！！！这样就简单很多！！！！
		'''

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            pos = self.map[val].pop()
            if not self.map[val]:
                del self.map[val]
            if pos != len(self.nums) - 1:
                self.map[self.nums[-1]][-1] = pos
                self.nums[pos], self.nums[-1] = self.nums[-1], self.nums[pos]
            self.nums.pop()
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()