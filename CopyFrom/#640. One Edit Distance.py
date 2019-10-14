#640. One Edit Distance

class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        m = len(s)
        n = len(t)
        if abs(m - n) > 1:
            return False
        if s == t:
            return False
        # ensure that s is a longer one
        if m < n:
            m, n = n, m
            s, t = t, s
        i = 0
        while i < min(m, n):
            if s[i] == t[i]:
                i += 1
            # find the first different position
            else:
                # insert or delete
                if s[i + 1:] == t[i:]:
                    return True
                # replace
                if s[i + 1:] == t[i + 1:]:
                    return True
                    
                return False
        # all the same except the last character in the longer string
        return True


-----
<Difference 三种情况讨论>
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        m = len(s)
        n = len(t)
        if s == t:
            return False
        # ensure that s is a longer one
        if m < n:
            m, n = n, m
            s, t = t, s
        diff = m - n
        
        if diff > 1: 
            return False
            
        if diff == 1:
            for i in range(n):
                if s[i] != t[i]:
                    return s[i+1:] == t[i:]
            return True
            
        if diff == 0:
            count = 0
            for i in range(n):
                if t[i] != s[i]:
                    count += 1 
            return count == 1
        
            
                