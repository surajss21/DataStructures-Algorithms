TC:- O(n)
SC:- O(n)
class Height:
    def __init__(self):
        self.h = 0
        
class Solution:
    def balanceOp(self, root, height):
        
        # Create left and right Heights objs
        lh = Height()
        rh = Height()
        
        # Base Case
        if(root == None):
            height.h = 0
            return True
        
        left = self.balanceOp(root.left, lh)
        right = self.balanceOp(root.right, rh)
        
        height.h = max(lh.h, rh.h) + 1
        
        diff = abs(lh.h - rh.h) <= 1
        
        if(left and right and diff):
            return True
        return False        
        
    def isBalanced(self,root):
        
        height = Height()        
        return self.balanceOp(root, height)
