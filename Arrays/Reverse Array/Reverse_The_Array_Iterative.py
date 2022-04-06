# Two Steps: 1. s = 0, e = n -1.
#            2. while(s<e) then swap(arr[s], arr[e])

def reverse(arr):
  s = 0
  e = len(arr)-1
  while(s<e):
    arr[s], arr[e] = arr[e], arr[s]
    s += 1
    e -= 1
 return arr
