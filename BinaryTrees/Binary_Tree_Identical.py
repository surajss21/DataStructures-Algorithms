class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,r1, r2):
        
        # Base Case 
        if(r1 == None and r2 == None):
            return True
        if(r1 == None and r2 != None):
            return False
        if(r1 != None and r2 == None):
            return False
            
        left = self.isIdentical(r1.left, r2.left)
        right = self.isIdentical(r1.right, r2.right)
        
        val = r1.data == r2.data
        
        if(left and right and val):
            return True
        return False
