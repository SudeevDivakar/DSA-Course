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
            
        queue = [root]
        
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')
        
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        #write code here
        if len(data) == 0:
            return None
            
        data = data.split(',')
        
        if data[0] == 'None':
            return None
        
        self.i = 1
        
        root = TreeNode(int(data[0]))
        
        queue = [root]
        
        while len(queue) > 0:
            node = queue.pop(0)
            
            if data[self.i] != 'None':
                node.left = TreeNode(int(data[self.i]))
                queue.append(node.left)
            self.i += 1
            
            if data[self.i] != 'None':
                node.right = TreeNode(int(data[self.i]))
                queue.append(node.right)
            self.i += 1 
            
        return root
    