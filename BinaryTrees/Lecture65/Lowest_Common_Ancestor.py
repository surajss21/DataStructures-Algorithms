def lowestCommonAncestor(root, x, y):
	
	# Base case.
	if(root == None):
		return None
	
	if(root.data == x or root.data == y):
		return root.data
	
	leftAns = lowestCommonAncestor(root.left, x, y)
	rightAns = lowestCommonAncestor(root.right, x, y)
	
	# 4 Cases
	if(leftAns != None and rightAns != None):
		return root.data
	elif(leftAns != None and rightAns == None):
		return leftAns
	elif(leftAns == None and rightAns != None):
		return rightAns
	else:
		return None
