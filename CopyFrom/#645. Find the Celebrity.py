#645. Find the Celebrity
思考：
要利用 knows(a, b) return False 的情况， 不仅仅用 True，不然就会TC = O(n^2) # 是不是所有人认识ta，ta不认识所有人

# worst case
(n-1) 次 可以‘屌丝化’一个人。 然后最后一个 O(n) 检查一次。

knows(a, b):
true  :  a knows b; 		 a is NOT Celebrity
false :  a do not know b     b is NOT Celebrity



class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        x = 0 # first as the presumed candiate
        for i in range(1, n):
            if Celebrity.knows(x, i):
                x = i
        
        # 把选出的人 做一次名人检验
        if any(Celebrity.knows(x, i) for i in range(n) if i != x) or any(not Celebrity.knows(i, x) for i in range(n)): return -1
            
        return 

        # i != x 名人会认识自己，别忘记了.