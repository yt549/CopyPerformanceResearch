#156. Merge Intervals
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if not intervals: return intervals
        intervals.sort(key = lambda x:x.start)
        lst = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start > lst[-1].end:
                lst.append(interval)
            else:
                lst[-1].end = max(lst[-1].end, interval.end)
                
        return lst
            