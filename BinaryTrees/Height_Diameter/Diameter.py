# T.C :- O(N^2)
# S.C :- O(Height)

def height(root):
        if(root == None):
            return 0
        
        left = height(root.left)
        right = height(root.right)
        ans = max(left, right) + 1
        return ans 
      
def diameter(root):
  # Base Case
  if(root == None):
    return 0
  opt1 = diameter(root.left)
  opt2 = diameter(root.right)
  opt3 = height(root.left) + height(root.right) + 1
  ans = max(opt1, opt2, opt3)
  return ans
