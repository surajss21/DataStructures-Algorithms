def height(root):
        # code here
        if(root == None):
            return 0
            
        left = height(root.left)
        right = height(root.right)
        
        ans = max(left, right) + 1
        return ans
