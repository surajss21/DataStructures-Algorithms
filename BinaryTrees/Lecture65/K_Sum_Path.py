class Solution:
    def solve(self, root, k, count ,path):
        # Base case 
        if(root == None):
            return
        
        path.append(root.data)
        
        #left
        self.solve(root.left, k, count, path)
        #right
        self.solve(root.right, k, count, path)
        
        sum = 0
        size = len(path)
        for i in range(size-1, -1, -1):
            sum += path[i]
            if(sum == k):
                count[0] += 1
        path.pop()
        
    def sumK(self,root,k):
        path = []
        count = [0]
        self.solve(root, k, count, path)
        return count[0]
