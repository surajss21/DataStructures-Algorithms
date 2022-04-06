def reverseLL(head):

  # Empty List
  if(head == None or head.next == None):
    return head
  else:
    curr = head
    prev = None
    forward = Node

    while(curr != None):
      forward = curr.next
      curr.next = prev
      prev = curr
      curr = forward
  return prev
