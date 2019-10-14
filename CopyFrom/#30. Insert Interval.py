#235. Prime Factorization

import math
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        factors = []
        for i in range(2, int(math.sqrt(num))+1):
            while num % i == 0:
                num = num // i
                factors.append(i)
        if num != 1:
            factors.append(num)
        return factors