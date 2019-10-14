#448. Inorder Successor in BST
<iteratively>
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        
       
        return successor

<Recursion>
def inorderSuccessor(self, root, p):
        if root is None or p is None:
            return None
            
        if p.val >= root.val:
            return self.inorderSuccessor(root.right,p)
        else:
            if self.inorderSuccessor(root.left,p) is None:
                return root
            else:
                return self.inorderSuccessor(root.left,p)