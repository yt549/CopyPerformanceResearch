#653. Expression Add Operators
'''
# 特殊判断：
	1. 第一个数字不能有符号 （+234-23）
	2. 数字不能前导为0 （234 + 034）


'''
class Solution:

    def addOperators(self, num, target):
        result = []
        total, lastF, tmp = 0, 0, ''
        self.dfs(target, num, total, lastF, tmp, result)
        return result
        
    def dfs(self, target, num, total, lastF, tmp, result):
    	# 退出条件
        if num == '':
            if target == total:
                result.append(tmp)
            return    	# 能不能更新，都要return
        
        curr = ''
        for i in range(len(num)):
            curr = int(num[:i+1])
            oldTotal, oldLastF, oldtmp = total, lastF, tmp
            # it's easer to take this condition out
            if tmp == '':    # 第一次不能有符号
                self.dfs(target, num[i+1:], curr, curr, str(curr), result)
                total, lastF, tmp = oldTotal, oldLastF, oldtmp
                
            else:
            	# 核心部分
                for op in ('+', '-', '*'):
                    if op == '+':
                        total = total + curr
                        lastF = curr
                        
                    elif op == '-':
                        total = total - curr
                        lastF = curr * -1
                        
                    elif op == '*':
                        total = total - lastF + lastF * curr
                        lastF = lastF * curr
                        
                    tmp = tmp + op + str(curr)
                    self.dfs(target, num[i+1:], total, lastF, tmp, result)
                    total, lastF, tmp = oldTotal, oldLastF, oldtmp   #backtracking
            
            # 不能有前导 ’0‘
            # test will fail without the following    
            if curr == 0:
                break


 乘号 X 时候：
 update sum：		 sum = sum - lastFactor + lastFactor * curr
 update lastFactor： lastFactor = lastFactor * curr

 加减 +- 时候：		 
 update sum：		 sum = sum +/- curr
 update lastFactor： lastFactor = curr * 1/-1





