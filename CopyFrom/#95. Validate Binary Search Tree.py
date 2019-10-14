#95. Validate Binary Search Tree
import sys
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        self.lastVal = -sys.maxsize
        self.firstNode = True
        self.isBST = True
        self.validate(root)
        return self.isBST
    
    def validate(self, node):
        if node is None: 
            return 
        self.validate(node.left)
        if self.lastVal >= node.val:
            self.isBST = False
            return 
        self.lastVal = node.val
        self.validate(node.right)
