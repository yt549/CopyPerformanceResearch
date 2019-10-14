#209. First Unique Character in a String

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        cnt = [0]*256
        for i in range(len(str)):
            cnt[ord(str[i])] += 1
        for i in range(len(cnt)):
            if cnt[i] == 1:
                return i
        return -1