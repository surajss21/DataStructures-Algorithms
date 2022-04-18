def noOfLeafNodes(root):

    if root is None:
        return 0

    if (root.left == None and root.right == None):
        return 1

    else:
        count = 0
        count = noOfLeafNodes(root.left) + noOfLeafNodes(root.right)
        return count
