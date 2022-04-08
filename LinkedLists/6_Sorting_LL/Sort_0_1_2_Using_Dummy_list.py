def sort_0_1_2_dummies(head):

  zeroHead = Node(-1)
  zeroTail = zeroHead
  oneHead = Node(-1)
  oneTail = oneHead
  twoHead = Node(-1)
  twoTail = twoHead
    
  curr = head
    
  while(curr != None):
      value = curr.data
        
      if(value == 0):
          zeroTail.next = curr
          zeroTail = curr
      elif(value == 1):
        oneTail.next = curr
        oneTail = curr
      elif(value == 2):
        twoTail.next = curr
        twoTail = curr
      curr = curr.next
    
  # Merging
  #IF 1's not empty
  if(oneHead != None):
    zeroTail.next = oneHead.next
  else:
      zeroTail.next = twoHead.next
        
  oneTail.next = twoHead.next
  twoTail.next = None
    
  #Set-up head
  head = zeroHead.next

  # Remove Dummies

  zeroHead.next = None
  oneHead.next = None
  twoHead.next = None
        
  return head
