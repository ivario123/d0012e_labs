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
        #### Return:
        list of 3 elements in ascending order
    """
    """
        if we have start == end we have reached the end of the recursion, and a list of 1 element
        since the element at index 0 in a list of one element is the smallest in that list we return
        a list containing that element and the largest values possible, since they cannot be in a regular list

        if this implementation is an issue then we can just add a check to see if the length of the list is sufficient.
    """
    if start == end:
        return [L[end], float('inf'), float('inf')]
    """
        Recursive call using an incremental approach. 
    """
    smallest = smallest_three_incremental(L, start+1, end)

    """
        Check where the current element fits into the list, 
        if we find and index, then insert it, else return list with
        no changes made
    """
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
    length = end-start+1
    """
        If we have start == end, we are at the end of the recursion, and have a list of length 1
        the elements at index 0 or index start is the smallest element in that list, thus returning this
        yields a sorted list of all the smallest elements in that list
    """
    if start == end:       # base case since a list of one element is sorted
        return [L[start]]

    """
        Since it is a divide and conquer algorithm we need to divide in to subproblems
        to do this we split the problem in halves, and record the left and the right results
    """
    mid = (start+end) // 2
    left = smallest_three_divide_and_conquer(L, start, mid)
    right = smallest_three_divide_and_conquer(L, mid+1, end)

    """
        Since we don't break at start-end == 3 we need to check lists shorter than 3 aswell.
        To know when we have checked every element in a list we need to know how long it is,
        since we cannot use len we use this.
    """
    if length < 6:                          # If length is les than 6 the sublists might not contain 3 elements, then we need to use the last loop
        left_len = mid-start+1              # If the length is les than 6 the left list contains mid-start+1 elements
        right_len = end-mid                 # .... end - mid elements
    else:
        left_len = 3
        right_len = 3
    max_value = 3

    """
        Defining the return variable ret
        this list will contain three or less elements never more. 
        if the length of the list is shorter than 3 elements we can know that the element in ret, 
        eventough less than 3 are the smallest elements in the list.
    """
    ret = []

    """
        Defining itteration variables:
            itter:
                keeps track of how many elements are in the list ret
            left_itter:
                keeps track of how many elements have been selected from the left list
            right_itter:
                ...... right list
    """
    itter = 0
    left_itter = 0
    right_itter = 0

    # Loop through lists, break if the lists are not equal length and one exceeded it's length
    # T(3) C Maximum number of itterations is 3. Thus this loop is constant time

    """
        Since max value is 3 this loop can only run for 3 itterations or less
        thus this is equivalent to 3 if statements and thus constant time

        if it exits before itter == max_len then:
            left_itter == left_len or right_itter == right_len
        and since only one of the itteration variables can be altered in an itteration
        we can be certain that one and only one of the next loops will be entered,
        thus resulting in constant time yet again.
    """
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

    """
        This loop is only entered when (left_max == left_itter|| right_max == right_itter) && itter!=3
        which gaurantees only 3 loops
    """
    if itter < max_value:                                           # Check that we have less than 3 elements
        """
            Since itter < max_value,  the previous for loop must have been exited with:
            (left_itter == left_len xor right_itter == right_len) == 1
            thus only one of these loops can execute
            and since max_value is 3, these loops can only run until 3 elements have been added
        """
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
        ### Param nums:  the vector we want to find the max subvector in
        ### Param left: the starting point for the left list
        ### Param right:  the ending point for the right list
        ### return list: [left_max, right_max, max_sum, sum_total]
        ### Breif
            finds the maximum subvector in a vector, using divide and conqure method.
        ### Stepwise
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
    """
    """
        if left == right then we have reached the end of the recursion and we have a list of length one. If that's the case then
        we know that the left sum is the current element, the right sum is the current element, the max sum is the current element
        and the entire array sum is the current element
    """
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

    """
        First we check if it's better to merge the entire left side with the left sum on the right side
            than to keep the left left sum
        then we check if it's better to merge the entire right side with the right sum of the left side
            than to keep the right right sum
        then we check if left_max > right_max and then we check if the largest one of them is larger than 
            the crossing sum ´i.e left right sum + right left sum´
        then we add the right sides sum and the left sides sum together to make the new sum.

        then return an array containing these keys
         
    """
    """
        Shorter implementation of the code below:

        left_max = max(left_sums[0],left_sums[3]+right_sums[0])
        right_max = max(right_sums[0],right_sums[3]+left_sums[0])
        max_sum = max(left_max,max(right_max,left_sums[1]+right_sums[0]))
        sum_total = leftsums[3]+right_sums[3]

        return [left_max,right_max,max_sum,sum_total]
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
