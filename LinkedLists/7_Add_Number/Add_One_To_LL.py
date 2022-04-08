def getDigit(head):
	
	temp = head
	num = 0	
	while(temp.next != None):
		val = temp.data
		num = (num * 10) + val
		temp = temp.next
	return num

def reverse(head):
	
	curr = head
	fwd = None
	prev = None
	while(curr != None):
		fwd = curr.next
		curr.next = prev
		prev= curr
		curr = fwd
	return prev
	

def addOneToList(head):
	
	if(head == None):
		return None
	
	ansHead = Node(-1)
	ansTail = ansHead
	
	num = getDigit(head)
		
	num = (num + 1)
	
	while(num != 0):
		rem = num % 10
		
		newNode = Node(rem)
		ansTail.next = newNode
		ansTail = newNode
		
		num = num//10
		
	ansHead = reverse(ansHead)
	
	return ansHead
