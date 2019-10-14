#649. Binary Tree Upside Down

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here
        if root is None:
            return root
        return self.dfs(root)
    
    def dfs(self, node):
        if node.left == None:
            return node
        newNode = TreeNode(node.left)
        newNode = self.dfs(node.left)
        
        node.left.right = node
        node.left.left = node.right
        # 至于为什么要写 if node.left == null 这句话，
        # 是因为 dfs在最后一个位置也就是4的时候，
		# 没有左节点节点（应题目要求），所以这是dfs的最后一层
        node.left = None
        node.right = None
        
        return newNode

    1						 
   / \
  2   3   
 / \
4   5

 ||
 
   4
  / \
 5   2
    / \
   3   1  

