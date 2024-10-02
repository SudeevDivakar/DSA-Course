# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return -1
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            d = left_height + right_height + 2
            diameter = max(diameter, d)

            return max(left_height, right_height) + 1

        dfs(root)

        return diameter
    
# Time Complexity = O(n)
# Space Complexity = O(d) where d -> depth of binary tree (space used by recursive call stack)