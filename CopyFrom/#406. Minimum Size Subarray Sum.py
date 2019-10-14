#406. Minimum Size Subarray Sum

挪动 i 的时候，看看 j 最多挪动到哪儿。
j 代表的是 subarray 右断点的 index + 1 的位置。因此 j - i 是 Subarray 的长度

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        n = len(nums)
        j = 0
        minSize = float('inf')
        sum = 0
        
        for i in range(n):
            while j < n and sum < s:
                sum += nums[j]
                j += 1          # j 不用回退到之前位置！prune
            if sum >= s:
                minSize = min(minSize, j-i)
            sum -= nums[i]
            
        return minSize if minSize != float('inf') else -1
            
            
            