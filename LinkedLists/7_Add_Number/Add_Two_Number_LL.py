def getDigit(head):
  
	temp = head
	num = 0
	
	while(temp != None):
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

def addTwoNumbers(head1, head2):
	
	ansHead = Node(-1)
	ansTail = ansHead
	
	head1 = reverse(head1)
	head2 = reverse(head2)
	
	num1 = getDigit(head1)
	num2 = getDigit(head2)
	
	res = num1 + num2
	
	while(res != 0):
		rem = res%10
    # Create Node 
		newNode = Node(rem)
		ansTail.next = newNode
		ansTail = newNode
		
		res = res//10
	
	ansHead = ansHead.next
	
	return ansHead
