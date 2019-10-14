#655. Add Strings

class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, number1, number2):
        # write your code here
        num1, num2 = list(number1), list(number2)
        carry, res = 0, []
        while len(num1) > 0 or len(num2) > 0:
            n1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0
            combine = n1 + n2 + carry
            res.append(combine%10)
            carry = combine // 10
        if carry:
            res.append(carry)
        return ''.join([str(i) for i in res])[::-1]