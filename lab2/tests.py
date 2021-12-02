from functions import *


"""
    This function is only for testing, it uses dynamic programming which is beyond the scope 
    of this course, howerver it is a dynamic programming sollution that runs in linear time,
    while only needing linear memory. Kinda neat.
"""
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
        L, ans): return smallest_three_incremental(L, 0, len(L)-1) == ans

    def assert_smallest_three_divide_and_conquer(
        L, ans): return smallest_three_divide_and_conquer(L, 0, len(L)-1) == ans

    def assert_max_subarray(L, ans): return max_subarray(
        L, 0, len(data)-1)[2] == ans

    print('~'*50+" Running tests "+'~'*50)
    data = list(np.random.randint(-1000, 1000, 100))
    smallest_three = smallest_three_incremental(data,0,len(data)-1)
    """
    Testing the min array
    """
    print("="*50+" smallest three incremental "+"="*50)
    print(
        f'Incremental approach to three smallest gave the ouput : {smallest_three_incremental([11,-2,1,2,3,4,5,6,7,8,9,10],0,11)}')
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
    data = list(np.random.randint(-100,100,1000000))
    r = maxSubArray(data)
    print(f'Dynamic programming sollution gives the output : {r}')
    print(
        f'Max subarray gives the output : {max_subarray(data,0,len(data)-1)}')
    worked = assert_max_subarray(data, r)
    print(
        f'Max subarray works : {worked} exptected {r}')
    # if not worked:
    #   print(f"For input : {data}")
    print("-"*50+" DONE "+"-"*50)
