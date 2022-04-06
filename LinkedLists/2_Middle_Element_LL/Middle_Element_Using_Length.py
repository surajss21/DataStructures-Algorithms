def getLength(head):
  
  count = 0
  temp = head
  while(temp != None):
    count += 1
    temp = temp.next
    
  return count

def getMiddle(head):

  len = getLength(head)
  ans = len//2
  cnt = 0
  temp = head

  while(cnt < ans):
    cnt += 1
    temp = temp.next   

  return temp

# Temp is a node
# cnt is index position
