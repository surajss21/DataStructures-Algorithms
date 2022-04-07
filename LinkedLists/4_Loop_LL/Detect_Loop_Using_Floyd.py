def detectLoop(head) :
    if(head == None or head.next == None):
        return False
      
    slow = head
    fast = head
    
    while(slow != None and fast != None):
        fast = fast.next
        if(fast != None):
            fast = fast.next
        slow = slow.next
        
        if(slow == fast):
            return True
        
    return False
