def sort_0_1_2(head):
  if(head == None or head.next == None):
    return None
  
  zeroCount = 0
  oneCount = 0
  twoCount = 0
	
  temp = head
	
  while(temp != None):
	  if(temp.data == 0):
		  zeroCount += 1
	  elif(temp.data == 1):
		  oneCount += 1
	  elif(temp.data == 2):
		  twoCount += 1
	  temp = temp.next
		
  temp = head
  while(temp != None):
	  if(zeroCount != 0):
		  temp.data = 0
		  zeroCount -= 1
	  elif(oneCount != 0):
		  temp.data = 1
		  oneCount -= 1
	  elif(twoCount != 0):
		  temp.data = 2
		  twoCount -= 1			
	  temp = temp.next
			
  return head
