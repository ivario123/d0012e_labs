from functions import *

assert_three_smallest_incremental = lambda L,ans: smallest_three_incremental(L) == ans
assert_smallest_three_divide_and_conquer = lambda L,ans: smallest_three_divide_and_conquer(L) == ans
assert_max_subarray = lambda L,ans: max_subarray(L) == ans
print(f'Incremental approch to three smallest gave the ouput : {smallest_three_incremental([11,-2,1,2,3,4,5,6,7,8,9,10])}')
print(f'Incremental approch to three smallest works : {assert_three_smallest_incremental([11,-2,1,2,3,4,5,6,7,8,9,10], [-2,1,2])}')
"""
  Testing the min array
"""
print(f'Divide and conquer approch to three smallest gave the output : {smallest_three_divide_and_conquer([11,-2,1,2,3,4,5,6,7,8,9,10])}')
print(f'Divide and conquer approch to three smallest works : {assert_smallest_three_divide_and_conquer([11,-2,1,2,3,4,5,6,7,8,9,10], [-2,1,2])}')

"""
  Testing the max array
"""

print(f'Max subarray gives the output : {max_subarray([-2,1,2,3,4,5,-10,6,7,8,9,10])}')
print(f'Max subarray works : {assert_max_subarray([-2,1,2,3,4,5,-10,6,7,8,9,10], sum([6,7,8,9,10]))}')