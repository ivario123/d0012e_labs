import math
import time
from matplotlib import pyplot as plt
import numpy
from math import log2
import sys
import os
import pandas as pd
import threading

"""
  insertion_sort(list):                                     #     
  for j = 2 to list.length                                  # C1    (n)
    key = list[j]                                           # C2    (n-1)
    //Insert n[j] into the sorted sequence list[1..j-1]     
    i = j-1                                                 # C3    (n-1)
    while i > 0 and list[i] > key                           # C4    ((n(n+1)/2)-1)
      list[i+1] = list[i]                                   # C5    (n(n-1)/2)
      i = i-1                                               # C6    (n(n-1)/2)
    list[i+1] = key                                         # C7    (n-1)

    T(n)= C1(n) + C2(n-1) + C3(n-1) + C4((n(n+1)/2)-1) + C5(n(n-1)/2) + C6(n(n-1)/2) + C7(n-1)

    Best case:  (C1 + C2 + C4 + C5 + C8) n – (C2 + C4 + C5 + C8)    O(n)
    Worst case: (C4/2 + C5/2 + C6/2)n^2 + (C1+ C2 + C3 + C4/2 - C5/2 - C6/2 + C7)n 
                - (C2 + C3 + C4 + C7)   O(n^2)
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
    l = len(lista)
    if l == 1:
        return lista

    # Dela listan i två delar
    mitten = len(lista)//2
    lista_1 = merge_sort(lista[0:mitten])
    lista_2 = merge_sort(lista[mitten:])
    return merge(lista_1, lista_2)

    # Slå samman de sorterade listorna (härska)


def merge_sort_l(list, n, k):
    l = len(list)
    if l <= k:       # We have reached the botom of the tree, where we have k lists
        return insertion_sort(list)
    middle = l//2

    right = merge_sort_l(list[middle:], n, k)
    left = merge_sort_l(list[:middle], n, k)
    return merge(left, right)


def merge(L1: list, L2: list):
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
    if len(lst) == 1:
        return lst
    for i in range(1, len(lst)):
        key = lst[i]
        position = binary_search(lst, i, key)
        lst.insert(position, key)
        del lst[i]
    return lst


def merge_sort_b(list, k):
    l = len(list)
    if l == 1 :
        return list
    if l <= k:       # We have reached the botom of the tree, where we have k lists
        return bSort(list)
    middle = l//2

    right = merge_sort_b(list[middle:], k)
    left = merge_sort_b(list[:middle], k)
    return merge(left, right)

