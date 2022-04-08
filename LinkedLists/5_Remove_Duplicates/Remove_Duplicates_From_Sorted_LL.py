def removeDuplicateSorted(head):
  # Empty List
  if(head == None):
    return None
  
  # Non empty list.
  curr = head

  while(curr != None):

    if((curr.next != None) and (curr.data == curr.next.data)):
      toDelete = curr.next
      curr.next = curr.next.next
      toDelete.next = None  
        
    else:
      curr = curr.next
  
  return head
