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

        queue = [root]

        while len(queue) > 0:
            node = queue.pop(0)

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return root

# Time Complexity = O(n)
# Space Complexity = O(n) because max width of queue can be n/2 (max number of leaf nodes)