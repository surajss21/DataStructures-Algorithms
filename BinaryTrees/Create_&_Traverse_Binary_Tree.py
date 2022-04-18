class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def buildTree(root):

	data = int(input("Enter The Data : "))
	root = Node(data)

	if(data == -1):
		return None

	print(f"Enter data for inserting in left of {data}")
	root.left = buildTree(root.left)
	print(f"Enter data for inserting in right of {data}")
	root.right = buildTree(root.right)

	return root

def levelOrderTravesal(root):
	q = []
	q.append(root)
	q.append(None)

	while(len(q) != 0):
		temp = q[0]
		q.pop(0)

		if(temp == None):
			print()
			if(len(q) != 0):
				q.append(None)

		else:
			print(temp.data, end = ' ')
			if(temp.left):
				q.append(temp.left)
			if(temp.right):
				q.append(temp.right)

def reverseLevelOrderTravesal(root):
	# Home Work
	pass

def inOrderTraversal(root): # L N R

	# Base Case
	if(root == None):
		return

	inOrderTraversal(root.left)
	print(root.data, end = ' ')
	inOrderTraversal(root.right)

def preOrderTraversal(root): # N L R

	# Base Case
	if(root == None):
		return

	print(root.data, end = ' ')
	preOrderTraversal(root.left)
	preOrderTraversal(root.right)

def postOrderTraversal(root): # L R N

	# Base Case
	if(root == None):
		 return

	postOrderTraversal(root.left)
	postOrderTraversal(root.right)
	print(root.data, end = ' ')

def buildFromLevelOrder(root):
	q = []
	data = int(input("Enter data for root : "))

	root = Node(data)
	q.append(root)

	while(len(q) != 0):
		temp = q[0]
		q.pop(0)

		leftData = int(input(f"Enter Left Node for {temp.data} : "))
		if(leftData != -1):
			temp.left = Node(leftData)
			q.append(temp.left)

		rightData = int(input(f"Enter Right Node for {temp.data} : "))
		if(rightData != -1):
			temp.right = Node(rightData)
			q.append(temp.right)

	return root


def main():

	root = None

	# Creating Tree
	root = buildTree(root)

	# Level Order Traversal
	print("\nThe Level Order Travesal is : ")
	levelOrderTravesal(root)

	# In-Order Traversal
	print("\nIn-Order Traversal")
	inOrderTraversal(root)

	# Pre-Order Traversal
	print("\nPre Order Traversal")
	preOrderTraversal(root)

	# Post-Order Traversal
	print("\nPost Order Traversal")
	postOrderTraversal(root)

	# Create Tree from Level Order
	print("Creating Tree From Level Order ")
	root = buildFromLevelOrder(root)
	levelOrderTravesal(root)


if __name__ == '__main__':
	main()
