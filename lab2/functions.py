"""
        TASK 1
"""



def smallest_three_incremental(L: list, start: int, end: int) -> list:
    if start == end:
        return [L[end], float('inf'), float('inf')]
    smallest = smallest_three_incremental(L, start+1, end)

    if L[start] < smallest[0]:
        smallest = [L[start], smallest[0], smallest[1]]
        return smallest
    if L[start] < smallest[1]:
        smallest = [smallest[0], L[start], smallest[1]]
        return smallest
    if L[start] < smallest[2]:
        smallest = [smallest[0], smallest[1], L[start]]
        return smallest
    return smallest


def smallest_three_divide_and_conquer(L: list, start: int, end: int) -> list:
    if start == end-3:
        smallest = L[start:end]

        if smallest[0] > smallest[1]:
            smallest[0],smallest[1] = smallest[1],smallest[0]
        if smallest[0]  > smallest[2]:
            smallest[0],smallest[2] = smallest[2],smallest[0] 
        if smallest[1] > smallest[2]:
           smallest[1],smallest[2] = smallest[2],smallest[1]

        return smallest
    mid = (start+end) // 2
    left = smallest_three_divide_and_conquer(L, start, mid)
    right = smallest_three_divide_and_conquer(L, mid+1, end)
    
    max_value = 3
    ret = []
    itter = 0
    left_itter = 0
    right_itter = 0

    while itter < max_value:  # This is equivalent to a number of if statements
        if left[left_itter] < right[right_itter]:
            ret.append(left[left_itter])
            left_itter += 1
        else:
            ret.append(right[right_itter])
            right_itter += 1
        itter += 1

    return ret


"""
        TASK 2
"""


def max_subarray(nums: list, left: int, right: int) -> list:
    if (left == right):
        return [nums[left], nums[left], nums[left], nums[left]]

    # ==================================== Divide ====================================
    # Get the left and right sums, divide
    middle = (left + right) // 2
    left_sums = max_subarray(nums, left, middle)            # Get the left values [left left sum, left right sum, left max sum, left sum ]
    right_sums = max_subarray(nums, middle + 1, right)      # Get the right values [right left sum, right right sum, right max sum, right sum]


    # ==================================== Conqure ====================================
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
