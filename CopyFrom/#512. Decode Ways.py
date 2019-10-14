#512. Decode Ways
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if len(s) == 0 or s[0] == '0': return 0
        dp = [0] * max(2, len(s)+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, len(s)+1):
            if 10 < int(s[i-2:i]) <= 26 and int(s[i-2:i]) != 20:
                dp[i] = dp[i-2] + dp[i-1]
            elif int(s[i-2:i]) == 20 or int(s[i-2:i]) == 10:
                dp[i] = dp[i-2]
            elif int(s[i-1]) != 0:
                dp[i]= dp[i-1]
            else:
                return 0
        return dp[-1]