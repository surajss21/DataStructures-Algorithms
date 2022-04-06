def getMinMax(arr, n):

  # Create minmax object
  min = 0
  max = 0

  # For 1 element
  if(n == 1):
    min = arr[0]
    max = arr[0]
    return (min, max)

  if(arr[0] < arr[1]):
    min = arr[0]
    max = arr[1]

  else:
    min = arr[1]
    max = arr[0]

  for i in range(2, n):
    if(arr[i] > max):
      max = arr[i]
    elif(arr[i] < min):
      min = arr[i]

  return (min, max)  

arr = [1,2,3,100,5,6,-7]
min, max = getMinMax(arr, len(arr))
print(min)
print(max)
