def detectLoop(head):

  if(head == None and head.next == None):
    return False

  lst = []
  temp = head

  while(temp != None):

    if(temp in lst):
      return True

    lst.append(temp)
    temp = temp.next

  return False
