# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if not root:
            return None

        def helper(node):
            if not node:
                return

            node.left, node.right = node.right, node.left
            helper(node.left)
            helper(node.right)

        helper(root)

        return root

# Time Complexity = O(n)
# Space Complexity = O(d) where d -> depth of binary tree (space used by recursive call stack)