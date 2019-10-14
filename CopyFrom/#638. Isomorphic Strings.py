#638. Isomorphic Strings

class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        return len(set(s)) == len(set(t)) and len(set(s)) == len(set(zip(s, t)))

---
<当标号仅是数字或者类数字('a', 'z')>
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        map = [False]*256
        for i in range(len(s)):
            if not map[ord(s[i])]:
                map[ord(s[i])] = t[i]
            else:
                if map[ord(s[i])] != t[i]:
                    return False
        return True

<仅类数字>
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        map = [False]*26
        for i in range(len(s)):
            if not map[ord(s[i])-ord('a')]:
                map[ord(s[i])-ord('a')] = t[i]
            else:
                if map[ord(s[i])-ord('a')] != t[i]:
                    return False
        return True

'''
笔记：
就是为了节省空间；要看String的组成类型。
如果是 （数字+类数字），可以initial 一个 256 长度的数组 （ascii max = 256)
如果是 （类数字），可以initial 一个 26 长度的数组。


