def kReverse(head, k):

  # Base Case
  if(head == None):
    return None
  
  # Step1 : Reverse k node
  forward = None
  curr = head
  prev = None
  count = 0
  while(curr != None and count < k):
    forward = curr.next
    curr.next = prev
    prev = curr
    curr = forward
    count += 1

  # Step2 : RC
  if(forward != None):
    head.next = kReverse(forward, k)

  # Return head
  return prev
