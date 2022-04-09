def reverse(head):
	curr =head
	fwd = None
	prev = None
	while(curr != None):
		fwd = curr.next
		curr.next = prev
		prev = curr
		curr = fwd
	return prev

def getDigit(head):
	
	temp = head
	num = 0
	while(temp != None):
		num = (num * 10) + temp.data
		temp = temp.next
	return int(num)

def multiplyLL(head1, head2):
	
	head1 = getDigit(head1)
	head2 = getDigit(head2)
	
	res = head1 * head2
	
	ansHead = Node(-1)
	ansTail = ansHead
	
	
	while(res != 0):
		rem = res % 10
		
		newNode = Node(rem)
		ansTail.next = newNode
		ansTail = newNode
		
		res = res//10
		
	ansHead = ansHead.next
	ansHead = reverse(ansHead)
	
	return ansHead
