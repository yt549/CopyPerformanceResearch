#652. Factorization

# 思考：
# 保证从小到大：
# 用start记录上一个枚举因子，本次枚举从上一次start开始。
# factor < remain; 即，factor1 <= factor 2 <= factor 3 <= ... <= remain.

import math
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        results = []
        self.dfs(results, [], n, 2)
        return results
    
    def dfs(self, results, path, n, start):
        if n == 1:
            if len(path) > 1:
                results.append(path[:])
            return

        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                path.append(i)
                self.dfs(results,path, n // i, i)
                path.pop()
        
        # 重点！如果有一个质数不能被分解。则需要解决的它
        # 比如 14 -> 2 & 7 where 7 > sqrt(14)
        if n >= start:
            path.append(n)
            self.dfs(results, path, 1, n)
            path.pop()
        
  ----

  import math
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        ans, path = [], []
        def dfs(start, remain):
            if remain == 1:
                if len(path)!= 1:
                    ans.append(path[:])
                return
        
            for i in range(start, remain):
                if i*i > remain:
                    break
                if remain % i == 0:
                    path.append(i)
                    dfs(start, remain//i)
                    path.pop()
            path.append(remain)
            dfs(n, 1)
            path.pop()
        
        dfs(2, n)
        return ans