#643. Longest Absolute File Path


class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """
    def lengthLongestPath(self, input):
        # write your code here
        if len(input) == 0:
            return 0
        ans = 0
        # 前缀和数组
        sum = [0]*(len(input)+1)
        for line in input.split('\n'):
            # 根据 \t 的个数. 看思考里的例子
            level = line.rfind('\t') + 2;
            # （level-1) = '\t' 的个数
            length = len(line) - (level - 1)
            if '.' in line: # 如果是文件
                # 前缀和长度 + 当前长度
                ans = max(ans, sum[level-1] + length)
            else: 
                # 如果是文件夹
                sum[level] = sum[level-1] + length + 1 # + 1 是 '\'
        return ans


---
思考
for example
input =  "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

representation:    
    dir
        subdir1
        subdir2
            file.ext

input.split('\n')
['dir', '\tsubdir1', '\tsubdir2', '\t\tfile.ext']
'''
level = line.rfind('\t') + 2
(if not exists '\t': # return -1)

s = '\t\tfile.ext'
print(s.rfind('\t'))
result = 1
'''
like 'dir': -1 + 2 = 1 --> level one

where levels are:
                    1
                    2
                    2
                    3


