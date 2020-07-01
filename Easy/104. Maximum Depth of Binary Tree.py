# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        leftLength = self.maxDepth(root.left) + 1
        rightLength = self.maxDepth(root.right) + 1

        return max(leftLength, rightLength)
