class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        #write code here
        
        res = []

        if not root:
            return ''

        def helper(node):
            if not node:
                res.append('_')
                return
            res.append(str(node.val))
            helper(node.left)
            helper(node.right)

        helper(root)
        
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        #write code here
        if len(data) == 0:
            return None

        data = data.split(',')
        
        self.i = 0

        def helper():
            if data[self.i] == '_':
                self.i += 1
                return None
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node
            
        return helper()
    