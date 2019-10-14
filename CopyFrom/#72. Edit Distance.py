#72. Edit Distance
https://www.jianshu.com/p/f01c2144ddb7

'''
使用九章算法强化班，动态规划专题班中讲过的匹配型动态规划
dp[i][j] 代表第一个字符串以i结尾匹配上（编辑成）第二个字符串以j结尾的字符串，最少需要多少次编辑。
通过去判断i与j的匹配关系来变为更小的状态。

  Ø a b c d
Ø 0 1 2 3 4
b 1 1 1 2 3
b 2 2 1 2 3
c 3 3 2 1 2

'''

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                    # equivalent to f[i][j] = f[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]
        

---
思考：
Q1: 如何理解d[i][j]的计算公式?
A1: 第(i,j)个位置的计算需要依赖于和它相邻的三个元素(i-1,j)、(i, j-1)和(i-1,j-1)，
	关键是哪一个对应删除，哪一个对应于插入，哪一个对应于替换？如果此时A[i]不等于B[j]，则（下面为全文最重要部分）:

	- 对于(i-1,j-1)时，d(i-1, j-1)表示完成从A[0,i-1]到B[0,j-1]的编辑次数，
	即现在A[0,i-1]=B[0,j-1]，对于(i,j)，我们直接把A[i]替换成B[j]即完成编辑。因此"(i-1,j-1)对应于把A[i]用B[j]替换的一次操作"

	- 对于(i-1, j)时，d(i-1, j)表示完成从A[0, i-1]到B[0, j]的编辑次数，即现在A[0,i-1]=B[0,j]，
	对于(i,j)，我们直接把A[i]删除即可完成编辑，因此"(i-1,j)对应于把A[i]删除的一次操作"

	- 对于(i, j-1)时，d(i, j-1)表示完成从A[0, i]到B[0, j-1]的编辑次数，即现在A[0,i]=B[0,j-1]，对于(i,j)，
	我们直接用B[j]插入到A[i]的位置即可完成编辑，因此"(i,j-1)对应于把B[j]插到A[i]的一次操作"



Q2： 为什么d是一个[m+1][n+1]大小的二维数组，为什么d数组要比字符串长度大一？

A2: 考虑A、B都为空字符串，我们还是需要一个[1][1]大小的数组记录其编辑距离为0。
	更进一步也就是说，我们假设字符串A为"AC"，则我们需要考虑['', 'A', 'AC']三种情况。



