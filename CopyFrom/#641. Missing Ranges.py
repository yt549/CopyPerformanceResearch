#641. Missing Ranges
class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        ans = []
        # edge case
        if not nums:
            self.addRange(ans, lower, upper)
            return ans
        # lower bound
        if nums[0] != -sys.maxsize:
            self.addRange(ans, lower, nums[0]-1)
        # middle bound
        for i in range(1, len(nums)):
            self.addRange(ans, nums[i-1]+1, nums[i]-1)
        # upper bound
        if nums[0] != sys.maxsize:
            self.addRange(ans, nums[-1]+1, upper)
        return ans
            
    def addRange(self, ans, st, ed):
        if st > ed: 
            return 
        elif st == ed:
            ans.append(str(st))
            return
        ans.append(str(st)+"->"+str(ed))
        

思考：
    如果是Java，需要考虑 maximum + 1 = minimum 的情况，
    所以用 if-statement 标注不会有 sys.maxsize 情况.maxsize
    python2 : sys.maxint 
    python3: sys.maxsize 
    注意区别