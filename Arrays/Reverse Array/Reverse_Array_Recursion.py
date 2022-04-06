def reverseArr(arr, s, e):
  # Base Case:
  if(s >= e):
    return   
  # Swap
  arr[s], arr[e] = arr[e], arr[s]
  # R.C
  reverseArr(arr, s+1, e-1)

arr = [1,2,3,4,5,6,7]
reverseArr(arr, 0, len(arr)-1)
print(arr)
