def reverse(head):
  if(head == None or head.next == None):
    return head

  curr = head
  fwd = None
  prev = None
  while(curr != None):
    fwd = curr.next
    curr.next = prev
    prev = curr
    curr = fwd

  return prev


def add(first, second):

  carry = 0

  ansHead = Node(-1)
  ansTail = ansHead

  while(first != None or second != None or carry != 0):

    val1 = 0
    if(first != None):
      val1 = first.data

    val2 = 0
    if(second != None):
      val2 = second.data

    sum = carry + val1 + val2 

    digit = sum % 10

    # Create Node Using digit
    newNode = Node(digit)
    ansTail.next = newNode
    ansTail = newNode

    print(ansTail.data)

    carry = sum//10

    if(first != None):
      first = first.next

    if(second != None):
      second = second.next

  ansHead = ansHead.next
  return ansHead

def addTwo(first, second):

  # Step 1 reverse LL
  first = reverse(first)
  second = reverse(second)

  # Step 2 add LL
  ans = add(first, second)

  ans = reverse(ans)

  return ans
