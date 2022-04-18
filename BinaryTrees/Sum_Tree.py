class Solution:
    def sumOp(self, root):
        
        if(root == None):
            return 0
            
        left = self.sumOp(root.left)
        right = self.sumOp(root.right)        
        ans = left + right + root.data
        
        return ans
        
        
    def isSumTree(self,root):
        
        if(root == None or (root.left == None and root.right == None)):
             return 1
        
        lsum = self.sumOp(root.left)
        rsum = self.sumOp(root.right)
        
        if((root.data == lsum + rsum) and self.isSumTree(root.left) and self.isSumTree(root.right)):
            return 1
        return 0
