def detectLoop(head):
    if(head == None or head.next == None):
        return None
    
    slow = head
    fast = head
    
    while(slow != None and fast != None):
        fast = fast.next
        if(fast != None):
            fast = fast.next
        slow = slow.next        
        if(slow == fast):
            return slow
    return None

def firstNode(head):
    if(head == None or head.next == None):
        return None  
     
    intersect = detectLoop(head)
    slow = head
    
    while(slow != intersect):
        slow = slow.next
        intersect = intersect.next
        
    return slow

print("The loop starts at",firstNode(head))
