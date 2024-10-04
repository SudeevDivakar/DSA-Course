# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        if not root:
            return True

        def helper(node, mini, maxi):
            if not node:
                return True

            value = node.val

            if value <= mini or value >= maxi:
                return False

            return helper(node.left, mini, value) and helper(node.right, value, maxi)

        return helper(root, -float('inf'), float('inf'))
    
# Time Complexity = O(n)
# Space Complexity = O(d) where d -> depth of binary tree (space used by recursive call stack)