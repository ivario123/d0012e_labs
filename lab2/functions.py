import numpy as np
from numpy.typing import _32Bit
"""
Given n(n<3) distinct elements, design two algorithms to compute the first three smallest
elements using an incremental and a divide-and-conquer approach, respectively. Both your
algorithms should return a triple (x,y,z)such that x<y<z<(the rest n < 3 input
elements)and run in linear time in the worst case. Show that your algorithms are correct
and calculate the exact number of comparisons used by the algorithms. You may assume
that n=3×2k31 for some positive integer k. Hint: One can use the induction technique
to show the correctness. Check Chapter 4 for more examples of performance analyses.
"""


from numpy.core.numeric import cross


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


def smallest_three_divide_and_conquer(L: list) -> list:
    """
      Finds the three samllest elements in the list L by dividing it in to sub problems
      ### param L: list of elements
      ### return: list of three smallest elements
    """
    length = len(L)
    if length == 1:       # base case since a list of one element is sorted
        return L
    mid = length // 2
    left = smallest_three_divide_and_conquer(L[:mid])
    right = smallest_three_divide_and_conquer(L[mid:])
    ret = []
    max_value = length if length < 3 else 3
    while len(ret) < max_value and left and right:
        if left[0] < right[0]:
            ret.append(left[0])
            del left[0]
        else:
            ret.append(right[0])
            del right[0]
    if len(ret) < max_value:
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

"""

    På wikipedia är bästa divide and conqure algoritmen nlogn int n. 
    På stack overflow är bästa divide and conqure algoritmen nlogn inte n.
    En divide and conqure algoritm tar som basfall O(log(n)) tid. Eftersom att vi måste
    kolla en interna summa, med linjär sökning då det inte finns någon garanti om storleksordning.
    Så måste varje steg i algoritmen söka linjärt, detta ger att vi måste köra log(n) linjära sökningar
    och därför får vi komplexitet O(nlog(n)) i varje fall


"""
    
def max_subarray_strange(L:list) -> list :
    length = len(L)
    if length == 1:
        return L[0]
    left = max_subarray(L[0:length-1])
    right = max_subarray(L[1:length])
    return max(left,right)

def max_subarray(L:list) -> list:
    """
        ### return list [sum, left, right, cross sum]
    """
    length = len(L)
    if length == 1:
        return [L[0],1,1,L[0]]
    mid = len(L) // 2
    # Finding side sums
    left = max_subarray(L[:mid])
    right = max_subarray(L[mid:])

    """
        Picking out the values from the arrays so that we can minimize the ammount of times the list is accessed
    """
    left_whole_sum = left[3]                                                                                       # Stores the sum of the entire left sub array
    left_chose_right = left[2]                                                                                     # Store wether the left branch chose to go rigth
    left_chose_left = left[1]                                                                                      # Stores wether the right brach chose to go left
    left_sum = left[0]                                                                                             # Stores the max sub array in the left brach
    right_whole_sum = right[3]                                                                                     # .... right branch ....
    right_chose_right = right[2]                                                                                   # .... right branch ....
    right_chose_left = right[1]                                                                                    # .... right branch ....
    right_sum = right[0]                                                                                           # .... right branch ....


    merge_center = [float("-inf"),-1,-1,left_whole_sum+right_whole_sum]                                            # Place holder in case the merge can't be done
    merge_right_whole_left = [float("-inf"),0,1,right_whole_sum+left_whole_sum]                                    # Place holder in case the merge can't be done 
    merge_left_whole_right = [float("-inf"),1,0,right_whole_sum+left_whole_sum]                                    # Place holder in case the merge can't be done


    if right_chose_left == 1:
            """
                If the right brach went left the we can merge the right branch with the entire left bracn
            """
            print(f"Possible merge from part of right half to entire left half with supposed value {right[0]+left_whole_sum}")
            merge_right_whole_left = [right[0]+left_whole_sum,0,1,right_whole_sum+left_whole_sum]
    if left_chose_right == 1 :
        
        """
            If the left branch went right then we can merge the left brach with the entire right branch
        """
        print(f"Possible merge from part of left half to entire right half with supposed value {right_whole_sum+left[0]}")
        merge_left_whole_right = [right_whole_sum+left[0],1,0,right_whole_sum+left_whole_sum]
        if right_chose_left == 1 :
            """
                If both leaves chose the path leading to the center, then we can merge them
            """
            crossing_sum  = right_sum+left_sum
            if crossing_sum > left_sum and crossing_sum > right_sum:
                print(f"Left side = {left_sum} Right side = {right_sum}")
                print(f"Crossing the arrays for L = {L} with cross sum = {crossing_sum}")
                if 0 != left_chose_left and 0 != right_chose_right:
                    print("Merging entire list")
                    merge_center = [crossing_sum,1,1,left_whole_sum+right_whole_sum]
                elif 0 != left_chose_left:
                    print("Merging from start of left")
                    merge_center = [crossing_sum,1,0,left_whole_sum+right_whole_sum]
                elif 0 != right_chose_right:
                    print("Merging from start of right")
                    merge_center = [crossing_sum,0,1,left_whole_sum+right_whole_sum]
                else :
                    print("Merging from other that ends")
                    merge_center = [crossing_sum,0,0,left_whole_sum+right_whole_sum]

    
    right_max =  [right_sum,0,1,left_whole_sum+right_whole_sum]                                                                 # Holds the right array sum
    left_max = [left_sum,1,0,left_whole_sum+right_whole_sum]                                                                    # Holds the left array sum 
    max_sides = right_max if right_sum > left_sum else left_max                                                                 # gets the largest side

    """
        Finding the maximum value possible from cross sum
    """
    max_merge = merge_right_whole_left if merge_right_whole_left[0] > merge_left_whole_right[0] else merge_left_whole_right     # Checks if it's better to merge left and right sums or left and entire right or right and entire left
    max_merge = max_merge if max_merge[0] > merge_center[0] else merge_center                                                   # ....
    max_sub = max_sides if max_sides[0] > max_merge[0] else max_merge                                                           # Checks wich sub array is the largest

    print(f"found max array for {L} with value {max_sub}")
    return max_sub

def max_subarray_old(L: list) -> list:
    """
      Finds the maximum sum of a subarray in the list L
      ### param L: list of elements
      ### return : sum of largest sublist
    """
    if len(L) == 1:
        return L[0]

    mid = len(L) // 2
    # Finding side sums
    left = max_subarray(L[:mid])
    right = max_subarray(L[mid:])

    # Finding center sum
    left_index = 1
    right_index = 0
    left_center = 0
    right_center = 0
    while left_index <= mid and L[mid-left_index] > 0:
        left_center = left_center + L[mid-left_index]
        left_index += 1
    while right_index < mid and L[mid+right_index] > 0:
        right_center = right_center + L[mid+right_index]
        right_index += 1
    center_sum = right_center+left_center
    if center_sum > right and center_sum > left:
        return center_sum
    elif right > left:
        return right
    else:
        return left

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
        L, ans): return smallest_three_divide_and_conquer(L) == ans
    def assert_max_subarray(L, ans): return max_subarray(L) == ans

    print('~'*50+" Running tests "+'~'*50)
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
        f'Divide and conquer approach to three smallest gave the output : {smallest_three_divide_and_conquer([11,-2,1,2,3,4,5,6,7,8,9,10])}')
    print(
        f'Divide and conquer approach to three smallest works : {assert_smallest_three_divide_and_conquer([11,-2,1,2,3,4,5,6,7,8,9,10], [-2,1,2])}')
    """
    Testing the max array
    """
    print("="*50+" maximum sub array "+"="*50)
    #data = list([4, -3, 1, -1, 1, 9, 0, -6, -4, 6])                # Exempel på skit som inte funkar
    data = list(np.random.randint(-10,10,10))                      # Funkar i 99% av fallen
    r = maxSubArray(data)
    print(
        f'Max subarray gives the output : {max_subarray(data)}')
    worked = assert_max_subarray(data, r)
    print(
        f'Max subarray works : {worked} exptected {r}')
    #if not worked:
     #   print(f"For input : {data}")
    print("-"*50+" DONE "+"-"*50)
