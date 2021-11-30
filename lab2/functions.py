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



def smallest_three_incremental(L: list) -> list:
    """ 
      Finds the three smallest elements in the list L
      ### param L : list of elements
      ### return : list of three smallest elements
    """
    if len(L) < 3:                                                  # C1
        return L                                                    # C2
    ret = [float('inf'), float('inf'), float('inf')]                # C3
    for el in L:                                                    # T(n)
        if el < ret[0]:                                             # C4
            ret[2] = ret[1]                                         # C5
            ret[1] = ret[0]                                         # C6
            ret[0] = el                                             # C7
        elif el < ret[1]:                                           # C8
            ret[2] = ret[1]                                         # C9
            ret[1] = el                                             # C10
        elif el < ret[2]:                                           # C11
            ret[2] = el                                             # C12
    return ret


def smallest_three_divide_and_conquer(L: list,start:int,end:int) -> list:
    """
      Finds the three samllest elements in the list L by dividing it in to sub problems
      ### param L: list of elements
      ### param start: start pointer, points to the first element in the list to look at
      ### param end: end pointer, points to the last element in the list to look at
      ### return: list of three smallest elements
    """

    """
        T(n) = sum(c_index) + 2*T(n/2) + 3* sum(c first while ) + 3 * sum ( c last if)   = sum(c_index) + 2*T(n/2)
    """
    length = end-start+1                                                                    # C
    if start == end:       # base case since a list of one element is sorted                # C 
        return [L[start]]                                                                   # C
    mid = (start+end) // 2                                                                  # C
    left = smallest_three_divide_and_conquer(L,start,mid)                                   # T(N/2)
    right = smallest_three_divide_and_conquer(L,mid+1,end)                                  # T(N/2)

    # Since we can't use length
    if length < 6 :                                                                         # C
        left_len = mid-start+1                                                              # C
        right_len = end-mid                                                                 # C
        max_value = length                                                                  # C
    else:                                           
        left_len = 3                                                                        # C
        right_len = 3                                                                       # C
        max_value = 3                                                                       # C
    
    # Defining itteration variables since we can't use if empty and such
    ret = []                                                                                # C
    itter = 0                                                                               # C
    left_itter = 0                                                                          # C
    right_itter = 0                                                                         # C

    # Loop through lists, break if the lists are not equal length and one exceeded it's length
    while itter < max_value and left_itter < left_len and right_itter < right_len:              # T(3) C Maximum number of itterations is 3. Thus this loop is constant time
        if left[left_itter] < right[right_itter]:                                               # T(3) C
            ret.append(left[left_itter])                                                        # T(3) C
            left_itter+=1                                                                       # T(3) C
        else:                                                                                   # T(3) C
            ret.append(right[right_itter])                                                      # T(3) C
            right_itter+=1                                                                      # T(3) C
        itter+=1                                                                                # T(3) C
    
    # Loop through the remaning list if one list ran out of numbers before filling result list
    if itter < max_value:                                                                       # C Maximum amount of loops is 3
        while left_itter < left_len:                                                            # T(< 3)
            ret.append(left[left_itter])                                                        # T(< 3) C
            left_itter+=1                                                                       # T(< 3) C
        while right_itter < right_len:                                                          # T(< 3)
            ret.append(right[right_itter])                                                      # T(< 3)C
            right_itter+=1                                                                      # T(< 3)C

    # Return the smallest numbers
    return ret                                                                                  # C


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

def max_subarray(nums:list,left:int,right:int) -> list :
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
        ### return values: left_max, right_max, max_sum, sum_total
    """
    # Base case, if left == right, i.e list ha 1 element, return that element at all indecies
    if (left == right):                                                                             # T(1)
        return [nums[left], nums[left], nums[left], nums[left]]                                     # C
    

    # ==================================== Divide ====================================
    # Get the left and right sums, divide
    middle = (left + right) // 2;                                                                   # T(1)
    left_sums = max_subarray(nums,left, middle);                                                    # T(N/2)
    right_sums = max_subarray(nums,middle + 1, right);                                              # T(N/2)

    # ==================================== Conqure ====================================
    # Log the max sum on the left side
    left_max = max(left_sums[0], left_sums[3] + right_sums[0])                                      # C

    # Log the max sum om the right side
    right_max = max(right_sums[1], right_sums[3] + left_sums[1])                                    # C

    # log the highest sum so far
    max_sum = max(left_sums[1] + right_sums[0], max(left_sums[2], right_sums[2]))                   # C

    # keep track of the entire sum
    sum_total = left_sums[3] + right_sums[3]                                                        # C


    return [left_max,right_max,max_sum,sum_total]                                                   # C


def maxSubArray(nums):
    """
    Dynamic programing for tests
    :type nums: List[int]
    :rtype: int
    """
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
    # print(dp)
    return max(dp)


if __name__ == "__main__":
    print('\\'*50+" STARTED "+'/'*50)
    print('~'*50+" Defining tests "+'~'*50)
    def assert_three_smallest_incremental(
        L, ans): return smallest_three_incremental(L) == ans
    def assert_smallest_three_divide_and_conquer(
        L, ans): return smallest_three_divide_and_conquer(L,0,len(L)-1) == ans
    def assert_max_subarray(L, ans): return max_subarray(L,0,len(data)-1)[2] == ans

    print('~'*50+" Running tests "+'~'*50)
    data = list(np.random.randint(-1000,1000,1000000))      
    smallest_three = smallest_three_incremental(data)
    """
    Testing the min array
    """
    print("="*50+" smallest three incremental "+"="*50)
    print(
        f'Incremental approach to three smallest gave the ouput : {smallest_three_incremental([11,-2,1,2,3,4,5,6,7,8,9,10])}')
    print(
        f'Incremental approach to three smallest works : {assert_three_smallest_incremental([11,-2,1,2,3,4,5,6,7,8,9,10], [-2,1,2])}')
    """
    Testing the min array
    """
    print("="*50+" smallest three divide and conqure "+"="*50)
    print(
        f'Divide and conquer approach to three smallest gave the output : {smallest_three_divide_and_conquer(data,0,len(data)-1)}')
    print(
        f'Divide and conquer approach to three smallest works : {assert_smallest_three_divide_and_conquer(data, smallest_three)}')
    """
    Testing the max array
    """
    print("="*50+" maximum sub array "+"="*50)                  




    r = maxSubArray(data)
    print(
        f'Max subarray gives the output : {max_subarray(data,0,len(data)-1)}')
    worked = assert_max_subarray(data, r)
    print(
        f'Max subarray works : {worked} exptected {r}')
    #if not worked:
     #   print(f"For input : {data}")
    print("-"*50+" DONE "+"-"*50)
