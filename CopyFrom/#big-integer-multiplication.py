#big-integer-multiplication/

# 数位相乘：
# 1. c[i+j] = a[i] * b[j]
# 2. 最后一次性进位

class Solution:
    # @param {string} num1 a non-negative integers
    # @param {string} num2 a non-negative integers
    # @return {string} return product of num1 and num2
    def multiply(self, num1, num2):
        # Write your code here
        l1 = len(num1)
		l2 = len(num2)
		ans = [0]*(len1 + len2 + 1)
		# 先不管进位
		for i in range(l1):
		    for j in range(l2):
		        ans[i+j] += int(num1[l1-i-1]) * int(num2[l2-j-1])

		for i in range(l1+l2):
		    ans[i+1] += ans[i]//10
		    ans[i] %= 10

		result2 = ""
		i = 0

		# ans.rstrip()
		while i < len(ans) - 1 and ans[i] == 0:
		    i += 1
		# convert to string
		while i < len(ans) - 1:
		    result2 += str(ans[i])
		    i += 1

		result2 = result2[::-1]
		return result2