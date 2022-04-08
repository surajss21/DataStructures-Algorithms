def sortTwoLists(first, second):
	
	if(first == None):
		return second
	if(second == None):
		return first
	
	ans = Node(-1)
	temp = ans
	
	while(first != None and second != None):
		if(first.data < second.data):
			temp.next = first
			temp = first
			first = first.next
		else:
			temp.next = second
			temp = second
			second = second.next
			
	while(first != None):
		temp.next = first
		temp = first
		first = first.next
		
	while(second != None):
		temp.next = second
		temp = second
		second = second.next
		
	ans = ans.next
	return ans
