def middle(head):
  if(head == None or head.next == None):
    return head

  fast = head.next
  slow = head
  while(fast != None):    
    fast = fast.next
    if(fast != None):
      fast = fast.next
    slow = slow.next
    
  return slow
