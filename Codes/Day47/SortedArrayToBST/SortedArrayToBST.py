# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        def helper(start, end):
            if start > end:
                return

            mid = (start + end) // 2
            node = TreeNode(nums[mid])

            node.left = helper(start, mid - 1)
            node.right = helper(mid + 1, end)

            return node
            
        return helper(0, len(nums) - 1)


# Time Complexity = O(n) - visit every node once and do constant time operations
# Space Complexity = O(n) - space used by the BST