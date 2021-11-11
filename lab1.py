
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

"""                                              costs           times
def binary_search(list, length, key):            
  low = 0                                        c1              O(1)
  high = length                                  c2              O(1)
  while low < high                               c3              log(n)
    mid = (low + high) / 2                       c4              log(n)*O(1)
    if list[mid] <= key                          c5              log(n)*O(1)
      low = mid + 1                              c6              log(n)*O(1)
    else
      high = mid                                 c7              log(n)*O(1)
  return low                                     c8              O(1)


T(n) = O(log(n))

"""

"""                                              costs           times
def bSort(list):
  for i = 1 to list.length                       c1              O(n)
    key = list[i]                                c2              n*O(1)
    position = binary_search(list, i, key)       c3              n*log(n)
    j = i                                        c4              n*O(1)
    while j > position                           c5              n*n       (n*O(1) if sorted) (O(n^2) if sorted in descending order)
      list[j] = list[j-1]                        c6              n*n*O(1)  (0      if sorted) (O(n^2) if sorted in descending order)
      j = j - 1                                  c7              n*n*O(1)  (0      if sorted) (O(n^2) if sorted in descending order)
    list[position] = key                         c8              n*O(1)
  return list                                    c9              O(1)


Worst case: T(n) = O(n^2)
Best case:  T(n) = O(n*log(n))

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
  #      O(n)   Will be used for merge sort calculations, since the  constants and factors won't matter much
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

def binary_search(lst, length, key):
  low = 0
  high = length
  while(low < high):
    mid = (low + high)//2
    if(lst[mid] <= key):
      low = mid + 1
    else:
      high = mid
  return low

def bSort(lst):
  for i in range(1, len(lst)):
    key = lst[i]
    position = binary_search(lst, i, key)
    j = i
    while(j > position):
      lst[j] = lst[j-1]
      j = j - 1
    lst[position] = key
  return lst

def merge_sort_b(list,n,k):
  if len(list) < n/k:       # We have reached the botom of the tree, where we have k lists
    return bSort(list)
  middle = len(list)/2
  
  right = merge_sort_b(list[middle:],n,k)
  left  = merge_sort_b(list[:middle],n,k)
  return merge(left,right)

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
