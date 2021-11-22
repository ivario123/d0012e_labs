
"""
Given n(n<3) distinct elements, design two algorithms to compute the first three smallest
elements using an incremental and a divide-and-conquer approach, respectively. Both your
algorithms should return a triple (x,y,z)such that x<y<z<(the rest n < 3 input
elements)and run in linear time in the worst case. Show that your algorithms are correct
and calculate the exact number of comparisons used by the algorithms. You may assume
that n=3×2k31 for some positive integer k. Hint: One can use the induction technique
to show the correctness. Check Chapter 4 for more examples of performance analyses.
"""


def smallest_three_incremental(L: list) -> list:
    """ 
      Finds the three smallest elements in the list L
      ### param L : list of elements
      ### return : list of three smallest elements
    """
    if len(L) < 3:
        return L
    ret = [float('inf'), float('inf'), float('inf')]
    for el in L:
      if el < ret[0]:
        ret.insert(0, el)
        ret.pop()
      elif el < ret[1]:
        ret.insert(1, el)
        ret.pop()
      elif el < ret[2]:
        ret.insert(2, el)
        ret.pop()
    return ret

def smallest_three_divide_and_conquer(L: list) -> list:
    """
      Finds the three samllest elements in the list L by dividing it in to sub problems
      ### param L: list of elements
      ### return: list of three smallest elements
    """
    if len(L) == 1:       # base case since a list of one element is sorted
        return L
    mid = len(L) // 2
    left = smallest_three_divide_and_conquer(L[:mid])
    right = smallest_three_divide_and_conquer(L[mid:])
    ret = []
    right_index = 0
    left_index = 0
    max_value = len(L) if len(L) < 3 else 3
    while len(ret) < max_value and len(left) > 0 and len (right) > 0:
      if left[0] < right[0]:
        ret.append(left[0])
        del left[0]
      else:
        ret.append(right[0])
        del right[0]
    if len(ret) != max_value:
      ret.extend(left)
      ret.extend(right)

    return ret


    

"""
Given an array A=a1,a2,···,an of non-zero real numbers, the problem is to find a
subarray ai,ai+1,···,aj  (of consecutive elements) such that the sum of all the numbers
in this subarray is maximum over all possible consecutive subarrays. Design a divide and
conquer algorithm to compute such a maximum sum. You do not need to actually output
such a subarray; only returning the maximum sum. Write only one recursive function to
implement your algorithm. Built-in functions or methods for strings or lists must not be
used. Your algorithm should run in O(n)time in the worst case. You may assume that
n=2k for some positive integer k.
"""
def max_subarray(L: list) -> int:
    """
      Finds the maximum sum of a subarray in the list L
      ### param L: list of elements
      ### return : sum of largest sublist
    """
    if len(L) == 1: # base case since a list of one elements max subsum is the element itself
        return L[0]
    mid = len(L) // 2
    left = max_subarray(L[:mid])
    right = max_subarray(L[mid:])
    
    # Checking if left sum is greater than right sum or if sum of left and right is greater than left and right
    if left + right> left and left + right > right:
        return left + right
    elif right > left:
        return right
    else:
        return left
        
