#639. Word Abbreviation

class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        # write your code here
        length = len(dict)
        ans = [False]*length
        prefix = [0]*length
        count = {}
        # 第一次 iteration
        for i in range(length):
            prefix[i] = 1
            ans[i] = self.getAbbr(dict[i], prefix[i]) 
            count[ans[i]] = count.get(ans[i], 0) + 1 
        # 只要有重复abbreviation，就一直iterate
        while True:
            unique = True
            for i in range(length):
                if count[ans[i]] > 1:
                    prefix[i] += 1 
                    ans[i] = self.getAbbr(dict[i], prefix[i])
                    count[ans[i]] = count.get(ans[i], 0) + 1
                    unique = False
            if unique:
                break
                
        return ans
        
    def getAbbr(self, s, p):
        # 如果不能变得更短，则放弃
        if p + 2 >= len(s):
            return s
        # 掐头去尾，算中间长度
        ans = s[:p] + str(len(s)-p-1) + s[-1]
        return ans