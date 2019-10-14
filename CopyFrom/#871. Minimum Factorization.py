#871. Minimum Factorization

import sys
class Solution:
    """
    @param a: a positive integer
    @return: the smallest positive integer whose multiplication of each digit equals to a
    """
    def smallestFactorization(self, a):
        # Write your code here
        res = 0
        base = 1
        for i in range(9, 1, -1):  # 越大越好
            while (a % i == 0):
                a //= i
                res += i * base
                
                # overflow 
                if res > sys.maxsize:
                    return 0

                base *= 10
            
        return res if res else 0
