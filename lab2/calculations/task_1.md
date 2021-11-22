# Incremental
## Algorithm
 - 1. Check if the length of the array is less than 3 if so return input array
 - 2. Declare a list ret with maximum integer values
 - 3. loop through the array
 - 4. if the current element is smaller than anny element in the ret list then insert it in the ret list at that index
 - 5. return ret

## proof of correctness


# Devide and Conquer
## Algorithm

  - 1. check if length of array is less than 1 if so return input array
  - 2. Call self with left and right halves of the array
  - 3. Select the 3 smallest elements in the return arrays ( both from left and right )
  - 4. return the 3 smallest elements

## proof of correctness
