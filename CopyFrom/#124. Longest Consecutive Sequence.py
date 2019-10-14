#124. Longest Consecutive Sequence

# 重点： 每个元素只访问了常数次。 所以是O(n)的算法。
# 比 先sort 再遍历，快了不知道多少~ (O(nlogn))
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, nums):
        # write your code here
        seen = set(nums)
        ans = 0
        for num in nums:
            if num in seen:
                seen.remove(num)
                pre, nxt = num - 1, num + 1
                while pre in seen:
                    seen.remove(pre)
                    pre -= 1
                while nxt in seen:
                    seen.remove(nxt)
                    nxt += 1
                ans = max(ans, nxt - pre - 1)
        return ans
        