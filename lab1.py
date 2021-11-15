
import time
import numpy
import pandas as pd
from functions import *
""" ================= Testing =================="""
# verify that a list is sorted
def is_sorted(l): return all(l[i] <= l[i+1] for i in range(len(l)-1))


def test_k() -> list:
    """
      Tests the different merge sort implementations based on the k value
      and a static n value.
    """
    ret = [
        ["merge_b_random"],
        ["merge_l_random"],
        ["k"]
    ]
    n = 2*10**4
    vals = list(numpy.random.randint(0, n, n))
    vals_sorted = sorted(vals)
    vals_almost_sorted = vals_sorted[:len(
        vals_sorted)//2]+vals[len(vals)//2::-1]
    for i in range(1, 500, 1):
        if is_sorted(vals):
            vals = list(numpy.random.randint(0, n, n))
        print(f"k test : Running tests for k = {i}", end='\r')
        # Testing merge sort with b sort
        t1 = time.time()
        merge_sort_b(vals, i)
        t2 = time.time()
        ret[0].append(t2-t1)
        # Testing merge sort with insertion sort
        t1 = time.time()
        merge_sort_l(vals, n, i)
        t2 = time.time()
        ret[1].append(t2-t1)

        # appending current k
        ret[2].append(i)

    df = pd.DataFrame(ret)
    df.to_csv('test_k.csv', index=False)
    print("Done with test_k")
    return ret


def test_random_case(k_1: int = 1, k_2: int = 1) -> list:
    """
        Tests the different merge sort implementations based on a static K value
        and a range of n values.
    """
    ret = [
        ["merge_l"],
        ["merge_b"],
        ["merge"],
        ["n"]
    ]

    for n in range(10**5, 10**6+1, 5*10**4):
        vals = list(numpy.random.randint(0, n, n))
        # Testing merge sort with insertion sort
        t1 = time.time()
        merge_sort_l(vals, n, k_1)
        t2 = time.time()
        ret[0].append(t2-t1)

        # Testing merge sort with bSort
        t1 = time.time()
        merge_sort_b(vals, k_2)
        t2 = time.time()
        ret[1].append(t2-t1)
        # Testing merge
        t1 = time.time()
        merge_sort(vals)
        t2 = time.time()
        ret[2].append(t2-t1)

        ret[3].append(n)
    print("Done with test_random_case")
    df = pd.DataFrame(ret)
    df.to_csv('test_random_case.csv', index=False)
    return ret


def test_medium_sorted_case(k_1: int = 1, k_2: int = 1) -> list:
    """
        Tests the different merge sort implementations based on a static K value
        and a range of n values.
        but with a semi sorted list

    """
    ret = [
        ["merge_l"],
        ["merge_b"],
        ["merge"],
        ["n"]
    ]

    for n in range(10**5, 10**6+1, 5*10**4):
        """ Creating a half sorted list """
        vals = list(range(0, n))
        vals[n//2:] = vals[n//2-1::-1]

        """ Testing merge sort with insertion sort """
        t1 = time.time()
        merge_sort_l(vals, n, k_1)
        t2 = time.time()
        ret[0].append(t2-t1)

        """ Testing merge sort with bSort """
        t1 = time.time()
        merge_sort_b(vals, k_2)
        t2 = time.time()
        ret[1].append(t2-t1)
        """ Testing merge """
        t1 = time.time()
        merge_sort(vals)
        t2 = time.time()
        ret[2].append(t2-t1)
        """ Storing current n """
        ret[3].append(n)
    df = pd.DataFrame(ret)
    df.to_csv('test_medium_sorted_case.csv', index=False)
    print("Done with test_medium_sorted_case")
    return ret


def test_big_random_case(k_1:int, k_2:int)->list:
    """
        Tests the different merge sort implementations based on a static K value
        and a range of n values.
        but with a large input length
    """
    ret = [
        ["merge_l"],
        ["merge_b"],
        ["merge"],
        ["n"]
    ]

    for n in range(10**5, 2*10**6, 2*10**5):
        vals = list(numpy.random.randint(0, n, n))
        """ Testing merge sort with insertion sort """
        t1 = time.time()
        merge_sort_l(vals, n, k_1)
        t2 = time.time()
        ret[0].append(t2-t1)

        """ Testing merge sort with bSort """
        t1 = time.time()
        merge_sort_b(vals, k_2)
        t2 = time.time()
        ret[1].append(t2-t1)

        """ Testing merge """
        t1 = time.time()
        merge_sort(vals)
        t2 = time.time()
        ret[2].append(t2-t1)

        ret[3].append(n)
    df = pd.DataFrame(ret)
    df.to_csv('test_big_random_case.csv', index=False)
    print("Done with test_big_random_case")
    return ret


def test_presorted_case(k_1:int, k_2:int) -> list:
    """
        Tests the different merge sort implementations based on a static K value
        and a range of n values.
        but with a presorted list
    """
    ret = [
        ["merge_l"],
        ["merge_b"],
        ["merge"],
        ["n"]
    ]

    for n in range(10**5, 10**6, 5*10**4):
        vals = list(range(0, n))
        # Testing merge sort with insertion sort
        t1 = time.time()
        merge_sort_l(vals, n, k_1)
        t2 = time.time()
        ret[0].append(t2-t1)

        # Testing merge sort with bSort
        t1 = time.time()
        merge_sort_b(vals, k_2)
        t2 = time.time()
        ret[1].append(t2-t1)
        # Testing merge
        t1 = time.time()
        merge_sort(vals)
        t2 = time.time()
        ret[2].append(t2-t1)

        ret[3].append(n)
    df = pd.DataFrame(ret)
    df.to_csv('test_presorted_case.csv', index=False)
    print("Done with test_presorted_case")
    return ret


def progress(percent: int) -> None:
    percent = int(percent)
    print(f"[{'='*percent}{' '*(100-percent)}] {percent}%", end='\r')


def test_presorted_case_insert() -> list:
    """
        Tests the different insertion sort implementations for 
        a range of n values.
        with a presorted list as argument
    """
    ret = [
        ["b_sort"],
        ["insertion"],
        ["merge"],
        ["n"]
    ]
    for n in range(1, 2*10**4+1, 500):
        print(f"Testing best for {n}", end='\r')
        nums = list(range(0, n))
        t1 = time.time()
        bSort(nums)
        t2 = time.time()
        ret[0].append(t2-t1)

        t1 = time.time()
        insertion_sort(nums)
        t2 = time.time()
        ret[1].append(t2-t1)

        t1 = time.time()
        merge_sort(nums)
        t2 = time.time()
        ret[2].append(t2-t1)

        ret[3].append(n)
    df = pd.DataFrame(ret)
    df.to_csv('test_presorted_case_insert.csv', index=False)
    print("Done with test_presorted_case_insert")
    return ret


def test_medium_case_insert() -> list:
    """
        Tests the different insertion sort implementations for
        a range of n values.
        but with a semi sorted list
    """
    ret = [
        ["b_sort"],
        ["insertion"],
        ["merge"],
        ["n"]
    ]
    for n in range(1, 2*10**4+1, 500):
        print(f"testing medium for {n}", end='\r')
        nums = list(range(0, n))
        nums[n//2-1:] = nums[n//2-1::-1]
        t1 = time.time()
        bSort(nums)
        t2 = time.time()
        ret[0].append(t2-t1)

        t1 = time.time()
        insertion_sort(nums)
        t2 = time.time()
        ret[1].append(t2-t1)

        t1 = time.time()
        merge_sort(nums)
        t2 = time.time()
        ret[2].append(t2-t1)

        ret[3].append(n)
    df = pd.DataFrame(ret)
    df.to_csv('test_medium_case_insert.csv', index=False)
    print("Done with test_medium_case_insert")
    return ret


def test_random_case_insert() -> list:
    """
        Tests the different insertion sort implementations for
        a range of n values.
        but with a random list
    """
    ret = [
        ["b_sort"],
        ["insertion"],
        ["merge"],
        ["n"]
    ]
    for n in range(1, 2*10**4+1, 500):
        print(f"testing random for {n}", end='\r')
        nums = list(numpy.random.randint(0, n, n))
        t1 = time.time()
        bSort(nums)
        t2 = time.time()
        ret[0].append(t2-t1)

        t1 = time.time()
        insertion_sort(nums)
        t2 = time.time()
        ret[1].append(t2-t1)

        t1 = time.time()
        merge_sort(nums)
        t2 = time.time()
        ret[2].append(t2-t1)
        ret[3].append(n)
    df = pd.DataFrame(ret)
    df.to_csv('test_random_case_insert.csv', index=False)
    print("Done with test_random_case_insert")
    return ret


if __name__ == "__main__":
    print("Started the tests")
    print("asserting that the functions work")
    """ Assertions to ensure that the code still works """
    print(is_sorted(merge_sort(list(range(0, 10)))))
    print(is_sorted(merge_sort_l(list(range(0, 10)), 10, 3)))
    print(is_sorted(merge_sort_b(list(range(0, 10)), 3)))
    """ Testing the elementary functions """
    print(test_presorted_case_insert())
    print(test_medium_case_insert())
    print(test_random_case_insert())
    print("Done with elementary tests")

    k = test_k()
    k_1, k_2 = 20, 786
    """ Testing the extended algorithms """
    print("Testing best case")
    test_presorted_case(k_1, k_2)
    print("Testing worst case")
    test_random_case(k_1, k_2)
    print("Testing semi sorted")
    test_medium_sorted_case(k_1, k_2)
    print("Testing big random")
    test_big_random_case(k_1, k_2)
