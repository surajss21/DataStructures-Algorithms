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

def getMiddle(head):
	slow = head
	fast = head.next
	while(fast != None and fast.next != None):
		slow = slow.next
		fast = fast.next.next		
	return slow
            
def isPalindrome(head):
	if(head == None):
		return True
	if(head.next == None):
		return True
	
	mid = getMiddle(head)	
	temp = mid.next
	mid.next = reverse(temp)
	
	head1 = head
	head2 = mid.next

	while(head2 != None):
		if(head1.data != head2.data):
			return False
		else:
			head1 = head1.next
			head2 = head2.next
			
	return True
