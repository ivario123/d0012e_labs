import numpy as np
"""
    Given n(n<3) distinct elements, design two algorithms to compute the first three smallest
    elements using an incremental and a divide-and-conquer approach, respectively. Both your
    algorithms should return a triple (x,y,z)such that x<y<z<(the rest n < 3 input
    elements)and run in linear time in the worst case. Show that your algorithms are correct
    and calculate the exact number of comparisons used by the algorithms. You may assume
    that n=3×2k31 for some positive integer k. Hint: One can use the induction technique
    to show the correctness. Check Chapter 4 for more examples of performance analyses.
"""


def smallest_three_incremental(L: list, start: int, end: int) -> list:
    """
        Finds the smallest 3 elements in a list using recursion. 
        #### Param L: 

        the list in wich we want to find the smallest three elements
        #### Param start: 

        where to start looking usually 0
        #### Param end: 

        where to stop looking usually len(L)-1
        #### Return 

        list of 3 elements in ascending order
    """

    if start == end:
        return [L[end], float('inf'), float('inf')]
    smallest = smallest_three_incremental(
        L, start+1, end)
    if L[start] < smallest[0]:
        smallest = [L[start], smallest[0], smallest[1]]
        return smallest
    if L[start] < smallest[1]:
        smallest = [smallest[0], L[start], smallest[1]]
        return smallest
    if L[start] < smallest[2]:
        smallest = [smallest[0], smallest[1], L[start]]
        return smallest
    # C
    return smallest


def smallest_three_divide_and_conquer(L: list, start: int, end: int) -> list:
    """
      Finds the three samllest elements in the list L by dividing it in to sub problems
      ### param L: list of elements
      ### param start: start pointer, points to the first element in the list to look at
      ### param end: end pointer, points to the last element in the list to look at
      ### return: list of three smallest elements
    """

    # C
    length = end-start+1
    if start == end:       # base case since a list of one element is sorted                # C
        # C
        return [L[start]]

    # C
    mid = (start+end) // 2
    left = smallest_three_divide_and_conquer(L, start, mid)
    right = smallest_three_divide_and_conquer(L, mid+1, end)

    # Since we can't use length
    if length < 6:
        left_len = mid-start+1
        right_len = end-mid
        max_value = length
    else:
        left_len = 3
        right_len = 3
        max_value = 3

    # Defining itteration variables since we can't use if empty and such
    ret = []
    itter = 0
    left_itter = 0
    right_itter = 0

    # Loop through lists, break if the lists are not equal length and one exceeded it's length
    # T(3) C Maximum number of itterations is 3. Thus this loop is constant time
    while itter < max_value and left_itter < left_len and right_itter < right_len:
        if left[left_itter] < right[right_itter]:
            ret.append(left[left_itter])
            left_itter += 1
        else:
            ret.append(right[right_itter])
            right_itter += 1
        itter += 1

    # Loop through the remaning list if one list ran out of numbers before filling result list
    # Maximum amount of loops is 2
    if itter < max_value:
        while left_itter < left_len and itter < max_value:
            ret.append(left[left_itter])
            left_itter += 1
            itter += 1
        while right_itter < right_len and itter < max_value:
            ret.append(right[right_itter])
            right_itter += 1
            itter += 1

    # Return the smallest numbers
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


def max_subarray(nums: list, left: int, right: int) -> list:
    """
        ## Breif
            finds the maximum subvector in a vector, using divide and conqure method.
        ## Stepwise
            -  if left == right return value at left
            -  go to first point with right = middle
            -  go to first point with left = midle +1
            -  set left max to the largest alternative

                choosing between the max on the left side or 

                the entire left side extended with right lists left max sum
            -  set right max to the largest alternative 

                choosing between the max on the right side or

                the entire right side extended with the left lists max sum

            - Set the max_sum to the largest alternative

                choosing between the maximum of the left and rights
                max sums or the left sides maximum to the right plus
                the right sides maximum to the left
            - Set the total sum equal to the sum of the left and right vector
        ### Param nums:  the vector we want to find the max subvector in
        ### Param left: the starting point for the left list
        ### Param right:  the ending point for the right list
        ### return values: [left_max, right_max, max_sum, sum_total]
    """
    # Base case, if left == right, i.e list ha 1 element, return that element at all indecies
    if (left == right):
        return [nums[left], nums[left], nums[left], nums[left]]

    # ==================================== Divide ====================================
    # Get the left and right sums, divide
    middle = (left + right) // 2
    left_sums = max_subarray(nums, left, middle)            # Get the left values [left left sum, left right sum, left max sum, left sum ]
    right_sums = max_subarray(nums, middle + 1, right)      # Get the right values [right left sum, right right sum, right max sum, right sum]


    # ==================================== Conqure ====================================

    """
        Array values are as follows: 
            [ left max:
                    either left sides left sum, or the crossing sum with the left hand side of the previous call and the right hand sides left side sum.
              right max:
                    either the right sides right sum or the crossing sum with the right hand side of the previous call and the left hand sides right sum.
              max : 
                    max(left max, max(right max, left sides right side max+ right sides left side max ´i.e crossing´))
              sum : 
                just the sum of the elements in the list, kinda neat, since it's used in two of 3 calculations
            ]
            
    
    """

    # Log the max sum on the left side
    if left_sums[0] > left_sums[3]+right_sums[0]:
        left_max = left_sums[0]                     # Case left left sum is better than merging entire left side with right left sum
    else:
        left_max = left_sums[3]+right_sums[0]       # Case mergin entire left side with right left sum is best

    # Log the max sum om the right side
    if right_sums[1] > right_sums[3]+left_sums[1]:
        right_max = right_sums[1]                   # Case right right sum is better than crossing entire right side with left right max
    else: 
        right_max = right_sums[3] + left_sums[1]    # Case merging entire right side with left right max is best

    # log the highest sum so far
    if left_sums[2] > right_sums[2]:
        max_temp = left_sums[2]                     # Case left sum was better than right sum
    else:
        max_temp = right_sums[2]                    # Case right sum was better than left sum

    if left_sums[1]+right_sums[0] > max_temp:
        max_sum = left_sums[1]+right_sums[0]        # Case crossing sum is better than both left and right
    else:
        max_sum = max_temp                          # Case left or right sum was best

    # keep track of the entire sum
    sum_total = left_sums[3] + right_sums[3]

    return [left_max, right_max, max_sum, sum_total]
