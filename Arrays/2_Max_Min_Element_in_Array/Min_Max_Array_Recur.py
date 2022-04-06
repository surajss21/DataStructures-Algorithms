# T.C O(N)
def getMinMax(arr, low, high):
  
  amin = 0
  amax = 0

  # Base Case.
  if(low == high):
    amin = arr[low]
    amax = arr[low]
    return (amin , amax)
  
  elif(high == low + 1):
    if(arr[low] > arr[high]):
      amax = arr[low]
      amin = arr[high]
    else:
      amin = arr[low]
      amax = arr[high]
    return (amin, amax)

  else:
    mid = (low + high)//2
    amin1, amax1 = getMinMax(arr, low, mid)
    amin2, amax2 = getMinMax(arr, mid+1, high)
    
  return (min(amin1, amin2), max(amax1, amax2))

arr = [1,2,3,100,5,6,-7]
minn, maxx = getMinMax(arr, 0, len(arr)-1)
print(minn)
print(maxx)
