class Solution:
    def solve(self, root, lenn, maxLen, summ, maxSum):
        # Base Case
        if(root == None):
            if(lenn > maxLen[0]):
                maxLen[0] = lenn
                maxSum[0] = summ
            elif(lenn == maxLen[0]):
                maxSum[0] = max(summ, maxSum[0])
            return
        
        summ = summ + root.data
        self.solve(root.left, lenn+1, maxLen, summ, maxSum)
        self.solve(root.right, lenn+1, maxLen, summ, maxSum)

    def sumOfLongRootToLeafPath(self,root):
        
        lenn = 0
        maxLen = [0]
        summ = 0
        maxSum = [-999999999999999999]
        
        self.solve(root, lenn, maxLen, summ, maxSum)
        
        return maxSum[0]
