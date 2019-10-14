#662. Guess Number Higher or Lower

class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        l, r = 1, n
        while l + 1 < r:
            mid = l + (r-l)//2
            if Guess.guess(mid) == 0: return mid
            elif Guess.guess(mid)  == 1: l = mid 
            else: r = mid 
        if Guess.guess(l)==0: 
            return l
        else: 
            return r