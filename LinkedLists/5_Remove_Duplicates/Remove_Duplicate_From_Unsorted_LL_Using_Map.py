def removeDuplicateUnsorted(head):

  if(head == None):
    return None

  lst = []

  curr = head
  lst.append(curr.data)

  while(curr.next != None):
    
    if(curr.next.data in lst):
      toDelete = curr.next
      curr.next = curr.next.next
      toDelete.next = None
    else:
      lst.append(curr.next.data)
      curr = curr.next

  return head
