def binary_search(lst, key):
  low = 0
  high = len(lst) - 1
  mid = 0

  while(low <= high):
    mid = (low + high) // 2
    if(low == high):
      # if low == high, but the key is larger than the middle number,
      # insert it to the right.
      if(key > lst[mid]):
        lst.insert(mid + 1, key)
        return lst
      else:
        lst.insert(mid, key)
        return lst
    elif(lst[mid] > key):
      high = mid - 1
    elif(lst[mid] < key):
      # inserts the key last if the key is the largest number
      if(mid == len(lst) - 1):
        lst.insert(mid+1, key)
        return lst
      low = mid + 1
    else:
      lst.insert(mid, key)
      return lst

# Testing:
#print(binary_search([1,2,4,7,8,9,10,10,15,19,26,73,89],7))

