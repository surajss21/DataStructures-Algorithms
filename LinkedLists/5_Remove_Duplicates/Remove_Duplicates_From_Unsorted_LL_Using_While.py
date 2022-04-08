def removeDuplicates(head):
	if(head == None):
		return None
	
	curr = head
	while(curr != None and curr.next != None):
		temp = curr
		while(temp.next != None):
			if(curr.data == temp.next.data):
				toDelete = temp.next
				temp.next = temp.next.next
				toDelete.next = None
			else:
				temp = temp.next
				
		curr = curr.next
		
	return head
