def reverseLL(head):
  
  # Base Case
  if(head == None or head.next == None):
    return head

  # R.c 
  chotaHead = reverseRec(head.next)

  head.next.next = head
  head.next = None

  return chotaHead


display(head)
head = reverseLL(head)
display(head)
