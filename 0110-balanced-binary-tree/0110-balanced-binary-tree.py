# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if root == None:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        def balanced(root):
            if not root:
                return True

            return (abs(height(root.left) - height(root.right)) < 2) and balanced(root.left) and balanced(root.right)
            
        return balanced(root)