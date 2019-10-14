#661. Convert BST to Greater Tree

# 反中序 DFS 遍历

class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        self.sum = 0
        self.helper(root)
        return root
        
    def helper(self, root):
        if root is None: 
            return 
        if root.right:
            self.helper(root.right)
        self.sum +=  root.val
        root.val = self.sum
        if root.left:
            self.helper(root.left)