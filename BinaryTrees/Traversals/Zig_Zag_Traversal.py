def zigZagTraversal(root):
	
	if(root == None):
		return []
	
	s1 = []
	s2 = []
	ans = []
	
	s1.append(root)
	
	leftToRight = True
	
	while(len(s1) != 0):
		temp = s1.pop()
		ans.append(temp.data)
		
		if leftToRight:
			if(temp.left):
				s2.append(temp.left)
			if(temp.right):
				s2.append(temp.right)
		else:
			if(temp.right):
				s2.append(temp.right)
			if(temp.left):
				s2.append(temp.left)
				
		if(len(s1) == 0):
			leftToRight = not leftToRight
			s1, s2 = s2, s1
			
	return ans
