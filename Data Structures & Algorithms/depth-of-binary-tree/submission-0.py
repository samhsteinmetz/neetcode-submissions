# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.helper(0, root)

    
    def helper(self, count, root):
        if root is None:
            return count

        
        count =max(self.helper((count+1),root.left),self.helper((count+1),root.right))

        return count
        

        