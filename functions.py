import math
import time
from matplotlib import pyplot as plt
import numpy
from math import log2
import sys
import os
import pandas as pd


""" ====================== Actual code ====================== """


def insertion_sort(list):
    """
    Sorts a list using insertion sort.
    """
    for j in range(1, len(list)):
        key = list[j]

        i = j-1
        while(i >= 0 and list[i] > key):
            list[i+1] = list[i]
            i = i-1
        list[i+1] = key
    return list


def merge_sort(list):
    """
    Sorts a list using merge sort.
    """
    l = len(list)
    if l == 1:
        return list

    # Dela listan i två delar
    middle = len(list)//2
    list_1 = merge_sort(list[0:middle])
    list_2 = merge_sort(list[middle:])
    return merge(list_1, list_2)

    # Slå samman de sorterade listorna (härska)


def merge_sort_l(list, n, k):
    """
    Sorts a list using merge sort.
    but sorts the sublists of length k with insertion sort
    """
    l = len(list)
    if l <= k:       # We have reached the botom of the tree, where we have k lists
        return insertion_sort(list)
    middle = l//2

    right = merge_sort_l(list[middle:], n, k)
    left = merge_sort_l(list[:middle], n, k)
    return merge(left, right)


def merge(L1: list, L2: list):
    """
      Sorts two lists by merging them.
    """
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
    """
    Searches for a key in a list using binary search.
    """
    low = 0
    high = length
    while(low <= high):
        mid = (low + high)//2
        if(lst[mid] < key):
            low = mid + 1
        elif lst[mid] > key:
            high = mid-1
        else:
            return mid

    return low


def bSort(lst):
    """
      Sorts a list using binary search.
    """
    if len(lst) == 1:
        return lst
    for i in range(1, len(lst)):
        key = lst[i]
        position = binary_search(lst, i, key)
        lst.insert(position, key)
        del lst[i]
    return lst


def merge_sort_b(list, k):
    """
      Sorts a list using binary search.
      but sorts the sublists of length k with bSort instead of insertion sort
    """
    l = len(list)
    if l == 1:
        return list
    if l <= k:       # We have reached the botom of the tree, where we have k lists
        return bSort(list)
    middle = l//2

    right = merge_sort_b(list[middle:], k)
    left = merge_sort_b(list[:middle], k)
    return merge(left, right)
