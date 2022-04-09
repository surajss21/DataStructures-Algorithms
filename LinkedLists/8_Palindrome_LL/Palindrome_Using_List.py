def isPalindrome(head):
	if(head == None):
		return True
	if(head.next == None):
		return True
	
	lst = []
	
	temp = head
	while(temp != None):
		lst.append(temp.data)
		temp = temp.next
		
	if(lst[::] == lst[::-1]):
		return True
	return False
