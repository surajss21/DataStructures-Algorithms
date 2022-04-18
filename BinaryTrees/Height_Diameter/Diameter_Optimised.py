class Height:
    
    def __init__(self):
        self.h = 0

class Solution:
    def diameterOp(self, root, height):
        
        # Store left, right Heights
        lh = Height()
        rh = Height()
        
        # Base Case
        if(root == None):
            height.h = 0
            return 0
            
        left = self.diameterOp(root.left, lh)
        right = self.diameterOp(root.right, rh)
        
        # Set the height of tree
        height.h = max(lh.h , rh.h) + 1
        
        # reutnr max(left, right, height)
        return max(lh.h + rh.h + 1, max(left, right))
        
    def diameter(self,root):
        
        height = Height()
        return self.diameterOp(root, height)
