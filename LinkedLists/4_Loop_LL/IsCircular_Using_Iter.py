def isCircularList(head):

  if(head == None):
    return True

  temp = head.next
  while(temp != None and temp != head):
    temp = temp.next
  if(temp == head):
    return True
  
  return False
