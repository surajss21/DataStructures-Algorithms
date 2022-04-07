def removeLoop(head :Node) -> Node :
    if(head == None):
        return head
    
    slow = head
    fast = head
    while(slow != None and fast != None):
        fast = fast.next
        if(fast != None):
            fast = fast.next
        slow = slow.next
        if(slow == None or fast == None):
            return head
        if(slow == fast):
            break
            
    itr = head
    while(slow != itr):
        slow = slow.next
        itr = itr.next
        if(itr == slow):
            break
            
    while(fast != None):
        if(fast.next == itr):
            fast.next = None
        fast = fast.next
        
    return head
