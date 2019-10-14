#650. Find Leaves of Binary Tree

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        # self.MaxDepth = 0
        ans = []
        self.depth = {}
        maxDepth = self.dfs(root)
        for i in range(1, maxDepth + 1):
            ans.append(self.depth[i])
        return ans
    
    def dfs(self, node):
        # find depth
        if node is None:
            return 0
        d = max(self.dfs(node.left), self.dfs(node.right)) + 1
        self.depth.setdefault(d, []).append(node.val)
        return d