#648. Unique Word Abbreviation

class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        # do intialization if necessary
        self.word = {}				# 记录word是否出现
        self.abbr = {}				# 记录abbreviation出现次数
        for word in dictionary:
            self.word[word] = 1
            sub = word[0] + str(len(word)-2) + word[-1]
            self.abbr[sub] = self.abbr.get(sub, 0) + 1
    
    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        if len(word) == 0:
            return True
        if len(word) == 1 or len(word) == 2:  		# 因为是dictionary，是个set。所以 word.size <= 2 一定为True
            return True 							# 因为压缩后长度不会变短，则不会有abbreviation产生。则一定Unique。
        sub = word[0] + str(len(word)-2) + word[-1] # 上面initialization忽略了 长度<=2 的情况。conditionally。因为查询时不会用到
        if word in self.word:						# 如果word出现在字典中，看是不是其abbreviation是唯一
            return self.abbr[sub] == 1
        if sub in self.abbr:						# 如果word不在字典中，但sub有。 如果原来本来就有，则必定重复
            return not self.abbr[sub]
        return True  								# else：return True (不在字典中，也不在abbr字典中的情况)
# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)