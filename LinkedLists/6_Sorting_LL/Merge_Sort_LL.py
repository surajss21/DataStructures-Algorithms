def findMid(head):

  if(head == None or head.next == None):
    return head

  slow = head
  fast = head.next
  while(fast != None and fast.next != None):
    fast = fast.next.next
    slow  = slow.next

  return slow

def merge(left, right):

  # Left is empty
  if(left == None):
    return right

  # Right is empty
  if(right == None):
    return left

  # Create dummy node
  ans = Node(-1)
  temp = ans

  # Merge 2 sorted LL
  while(left != None and right != None):

    if(left.data < right.data):
      temp.next = left
      temp = left
      left = left.next

    else:
      temp.next = right
      temp = right
      right = right.next

  
  # if left list is not empty
  while(left != None):
    temp.next = left
    temp = left
    left = left.next

  # if right list is not empty
  while(right != None):
    temp.next = right
    temp = right
    right = right.next

  ans = ans.next
  return ans

def mergeSort(head):

  # Base Case
  if(head == None or head.next == None):
    return head

  # Break LL into two halfs.
  mid = findMid(head)
  left = head
  right = mid.next
  mid.next = None

  # R.C to sort both halfs
  left = mergeSort(left)
  right = mergeSort(right)

  # Merge left and right
  res = merge(left, right)

  return res
