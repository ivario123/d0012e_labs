
import time
from matplotlib import pyplot as plt
import numpy
from math import log2
import sys, os

"""
  insertion_sort(list):
  for j = 2 to list.length
    key = list[j]
    //Insert n[j] into the sorted sequence list[1..j-1]
    i = j-1
    while i > 0 and list[i] > key
      list[i+1] = list[i]
      i = i-1
    list[i+1] = key
"""

"""
  binary_search(list, key):
  int mid = len(list)//2
  // check middle
  if(list[mid] < list[mid-1])
    binary_search(list[mid//2], key)
  
  // divide by 2 if key can't be placed
"""

"""
  bSort(list)
    for index from 1 to length of list
      key = list[index]
      
      
"""

"""
Spiffis take on binary search doing binary sort.

binarySearch(list, n, key)
    L = 0
    R = n
    while L < R
        mid = (L + R)/2
        if list[mid] <= key:
            L = mid + 1
        else:
            R = mid
    return L

binaryInsertionSort(list)
    for i = 1 to list.length
        key = list[i]
        pos = binarySearch(list, key, 0, i-1)
        j = i
        while j > pos
            Array[j] = Array[j-1]
            j = j-1
        list[pos] = key
"""

"""
  def merge_sort_b(list,n,k):
    if len(list) < n/k:       # We have reached the botom of the tree, where we have k lists
      return bSort(list)
    middle = len(list)/2
  
    right = merge_sort_b(list[middle:],n,k)
    left  = merge_sort_b(list[:middle],n,k)
    return merge(left,right)
"""

"""
  def merge_sort_l(list,n,k):                # T1(n)
    if len(list) <= k:                       # We have reached the botom of the tree, where we have k lists
      return insertion_sort(list)            # O(n^2)
    middle = len(list)//2                    # C1
    
    right = merge_sort_l(list[middle:],n,k)  # T1( floor( n/2 ))
    left  = merge_sort_l(list[:middle],n,k)  # T1( floor( n/2 ))
    return merge(left,right)                 # t_merge = O(n)
  T(n) =   O(k^2) if  n <= k
           c1+2*T(floor(n/2)) + O(n) if n > k
  


"""
"""
  
def merge(L1, L2):
    merged = []                           #O(1)
    while(len(L1) >0and len(L2)>0):       #T1(n*2)                 ( Worst case 2*n )
        if L1[0] > L2[0]:                 #O(1)
          merged.append(L2[0])            #C1
          L2.pop(0)                       #C2
        else:
          merged.append(L1[0])            #C3
          L1.pop(0)                       #C4
    merged+=L1                            #C5 O(n)        
    merged+=L2                            #C6 O(n)
    return merged
  #T(n) = f_5*C5+f_4*C6+1\sum_1^(2*n) (f_1*(C1+C2)+f_2*(C3+C4)+1) = f_5*C5+f_4*C6+1 + (2*n-1)*(f_1*(C1+C2)+f_2*(C3+C5)+1) = 
  #      
  #      O(n)
  #
  #
  #where f_1 = percentage of L1 that is larger than L2
  #      f_2 = 1-f_1
  #      f_3 = number of elements left in L1 after merging elements 
  #      f_4 = len(L1)-f_3 {since len(L1) == len(L2)}

"""


""" ====================== Actual code ====================== """


def insertion_sort(list):
    for j in range(1, len(list)):
        key = list[j]

        i = j-1
        while(i >= 0 and list[i] > key):
            list[i+1] = list[i]
            i = i-1
        list[i+1] = key
    return list


def merge_sort(lista):
    if len(lista) == 1:
        return lista

    # Dela listan i två delar
    mitten = len(lista)//2
    lista_1 = merge_sort(lista[0:mitten])
    lista_2 = merge_sort(lista[mitten:])
    return merge(lista_1, lista_2)

    # Slå samman de sorterade listorna (härska)


def merge_sort_l(list, n, k):
    if len(list) <= k:       # We have reached the botom of the tree, where we have k lists
        return insertion_sort(list)
    middle = len(list)//2

    right = merge_sort_l(list[middle:], n, k)
    left = merge_sort_l(list[:middle], n, k)
    return merge(left, right)


def merge(L1, L2):
    merged = []  # O(1)
    while(len(L1) and len(L2)):  # T1(n*2)
        if L1[0] > L2[0]:  # O(1)
            merged.append(L2[0])  # C3
            L2.pop(0)  # C4
        else:
            merged.append(L1[0])  # C5
            L1.pop(0)  # C6
    merged += L1
    merged += L2
    return merged


def binary_search(lst, key):
  os.system('cls')
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


# ================= Testing ==================
# verify that a list is sorted
is_sorted = lambda l: all(l[i] <= l[i+1] for i in range(len(l)-1))


def test_merge_sort():
    # log_10(n)
    i_range = (2,15)
    # k values to test
    j_range = (1,100)
    # plot optimal k values for different n
    optimal_k = []
    for i in range(i_range[0],i_range[1]):
      # Store the execution times for the 2 implementations
      merge_sort_1 = []
      merge_sort_2 = []
      # Store difference between implementations
      delta_time = []
      # Track the best K val
      max_diff = 0
      max_diff_k = 0
      # Keep the distrobition consitant between K changes
      nums = numpy.random.random_integers(0, 100, 2**i).tolist()
      x_values = []
      # this should be the optimal size
      print(f"log2({2**i}) = {log2(2**i)}")
      for j in range(j_range[0],j_range[1]):
        x_values.append(j)
        # generate a random list of integers
        # check how long time the default merge sort takes
        t1 = time.time()
        merge_sort(nums)
        t2 = time.time()
        dt = t2-t1
        merge_sort_1.append(dt)

        # decalare the number of elements in lists
        n = 2**i
        k = j
        # check how long time it takes to run our merge sort
        t1 = time.time()
        merge_sort_l(nums, n, k)
        t2 = time.time()
        if dt-(t2-t1) > max_diff:
          max_diff_k=k
          max_diff = dt-(t2-t1)
        delta_time.append(dt-(t2-t1))
        merge_sort_2.append(t2-t1)
        progress(100*((i-i_range[0])*(j_range[1]-j_range[0])+j-j_range[0])/((i_range[1]-i_range[0])*j_range[1]-j_range[0]))
      optimal_k.append(max_diff_k)
      print(f"Optimal K for N = {2**i} is {max_diff_k}",end = '\r')


      # Plot the measured values
      plt.plot(merge_sort_1,x_values,label = "merge_standard")
      plt.plot(merge_sort_2,x_values,label = "merge_linear")
      plt.legend()
      plt.title("Merge sort time effeciency")
      plt.xlabel("delta t")
      plt.ylabel("K")
      plt.show()
    #plt.plot(list(range(i_range[0],i_range[1]),optimal_k))
    #plt.xlabel("Input range")
    #plt.ylabel("Optimal K value")
    #plt.show()

def progress(percent:int):
  percent = int(percent)
  print(f"[{'='*percent}{' '*(100-percent)}] {percent}%",end = '\r')

if __name__ == "__main__":
  print("Started the tests")
  test_merge_sort()
