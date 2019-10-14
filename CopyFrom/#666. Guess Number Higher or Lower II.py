#666. Guess Number Higher or Lower II

class Solution:
    """
    @param n: An integer
    @return: how much money you need to have to guarantee a win
    """
    def getMoneyAmount(self, n):
        # write your code here
        dp = [[0]*(n+1) for _ in range(n+1)]
        def solve(lo, hi):
            if lo < hi and dp[lo][hi] == 0:
                dp[lo][hi] = min(x + max(solve(lo, x-1), solve(x+1, hi)) for x in range(lo, hi))
            return dp[lo][hi]
        return solve(1, n)