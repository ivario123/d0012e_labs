
import time
import numpy
from math import log2
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
  def merge_sort_l(list,n,k):
    if len(list) <= k:       # We have reached the botom of the tree, where we have k lists
      return insertion_sort(list)            O(n^2)
    middle = len(list)//2                    C1
    
    right = merge_sort_l(list[middle:],n,k)  T1
    left  = merge_sort_l(list[:middle],n,k)  T2
    return merge(left,right)                 O(n)

"""
"""
  def merge(L1, L2):
    merged = []                           O(1)
    for i in range(0, len(L1)+len(L2)-1): T1(n*2)
        if len(L1) == 0:                  O(1)
          merged.extend(L2)               C1
          return merged                   
        elif len(L2) == 0:                O(1)
          merged.extend(L1)               C2
          return merged                   
        elif L1[0] > L2[0]:               O(1)
          merged.append(L2[0])            C3
          L2.pop(0)                       C4
        else:
          merged.append(L1[0])            C5
          L1.pop(0)                       C6
    return merged
  T(n) = 
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

def merge_sort( lista ):
  if len( lista ) == 1:
    return lista

  #Dela listan i två delar
  mitten = len(lista)//2
  lista_1 = merge_sort( lista[0:mitten] )
  lista_2 = merge_sort( lista[mitten:] )
  return merge(lista_1,lista_2)

  #Slå samman de sorterade listorna (härska)
  
def merge_sort_l(list,n,k):
  if len(list) <= k:       # We have reached the botom of the tree, where we have k lists
    return insertion_sort(list)
  middle = len(list)//2
  
  right = merge_sort_l(list[middle:],n,k)
  left  = merge_sort_l(list[:middle],n,k)
  return merge(left,right)


def merge(L1, L2):
    retur_lista = []
    while len( L1 ) > 0 and len( L2 ) > 0:
      if L1[0] < L2[0]:
        retur_lista.append( L1[0] )
        L1.pop(0)
      else:
        retur_lista.append( L2[0] )
        L2.pop(0)

    #Lägg till de element som "blev över" i slutet
    retur_lista += L1
    retur_lista += L2
    return retur_lista


# verify that a list is sorted 
is_sorted = lambda l : all(l[i] <= l[i+1] for i in range(len(l)-1))
# generate a random list of integers
nums = numpy.random.random_integers(0,100,1000000).tolist()
# check how long time the default merge sort takes
t1 = time.time()
l = merge_sort(nums)
t2 = time.time()
# log data
print(f"is sorted {is_sorted(l)}")
print(f"merge sort delta T = {t2-t1}")

# decalare the number of elements in lists
n = len(nums)
k = log2(n)
# check how long time it takes to run our merge sort
t1 = time.time()
l = merge_sort_l(nums,n,k)
t2 = time.time()

# log data
print(f"is sorted {is_sorted(l)}")
print(f"merge sort {k} lists delta T = {t2-t1}")