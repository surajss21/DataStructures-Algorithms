# T.C : O(n^2)
# S.C : O(height)

class Solution:
    def height(self, root):
        if(root == None):
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        
        ans = max(left, right) + 1
        return ans
        
    def isBalanced(self,root):
        
        if(root == None):
            return True
            
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        
        diff = abs(self.height(root.left) - self.height(root.right)) <= 1
        
        if(left and right and diff):
            return True
        else:
            return False
