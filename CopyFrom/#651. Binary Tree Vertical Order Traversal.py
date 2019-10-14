#651. Binary Tree Vertical Order Traversal

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        import collections
        results = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, x = queue.popleft()
            if node:
                results[x].append(node.val)
                queue.append((node.left, x-1))
                queue.append((node.right, x+1))
        
        return [results[i] for i in sorted(results)]. # dictionary 可以 sort！！
        