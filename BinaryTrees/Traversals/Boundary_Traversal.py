def traverseLeft(root, ans):
	
	# Base case
	if(root == None):
		return
	
	if(root.left == None and root.right == None):
		 return
		
	ans.append(root.data)
	
	if(root.left):
		traverseLeft(root.left, ans)
	else:
		traverseLeft(root.right, ans)
		
def traverseLeaf(root, ans):
	
	# Base Case
	if(root == None):
		return
	
	if(root.left == None and root.right == None):
		ans.append(root.data)
		return
	traverseLeaf(root.left, ans)
	traverseLeaf(root.right, ans)
	
def traverseRight(root, ans):
	# BAse case
	if(root == None ):
		return
	if(root.left == None and root.right == None):
		return
	
	if(root.right):
		traverseRight(root.right, ans)
	else:
		traverseRight(root.left, ans)
	
	# Wapus aareyho
	ans.append(root.data)

def traverseBoundary(root):
	
	ans = []
	
	if(root == None):
		return ans
	
	ans.append(root.data)
	
	# Part 1:- Print all left except leaf nodes
	traverseLeft(root.left, ans)
	
	# Part2:- leaf node
	# left part
	traverseLeaf(root.left, ans)
	# right part
	traverseLeaf(root.right, ans)
	
	# Part 3 :- print all right except leaft node
	traverseRight(root.right, ans)
	
	return ans
