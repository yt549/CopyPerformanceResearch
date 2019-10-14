#659. Encode and Decode Strings

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = []
        for s in strs:
            for char in s:
                if char == ':':
                    res.append("::")
                else:
                    res.append(char)
            res.append(":;")
        return ''.join(res)
            
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res, temp, i = [], [], 0
        while i < len(str)-1:
            if str[i] == ':':
                if str[i+1] == ':':
                    temp.append(':')
                    i += 2
                elif str[i+1] == ';':
                    res.append(''.join(temp))
                    temp = []
                    i += 2
            else:
                temp.append(str[i])
                i += 1
        return res
                    