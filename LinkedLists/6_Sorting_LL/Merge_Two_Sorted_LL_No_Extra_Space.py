def solve(first, second):
    
    # One element
    if(first.next == None):
        first.next = second
        return first
    
    curr1 = first
    next1 = curr1.next
    curr2 = second
    next2 = curr2.next
    
    while(next1 != None and curr2 != None):
        
        if((curr2.data >= curr1.data) and (curr2.data <= next1.data)):
            # adding node
            curr1.next = curr2
            next2 = curr2.next
            curr2.next = next1
            #updating pointer
            curr1 = curr2
            curr2 = next2            
            pass
        else:
            curr1 = next1
            next1 = next1.next
            
            if(next1 == None):
                curr1.next = curr2
                return first
            pass
    return first
      
def sortTwoLists(first, second):
    # Write your code here.
    
    if(first == None):
        return second
    if(second == None):
        return first
    
    if(first.data <= second.data):
        return solve(first, second)
    else:
        return solve(second, first)
    pass
