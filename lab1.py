
from functions import *
""" ================= Testing =================="""
# verify that a list is sorted
def is_sorted(l): return all(l[i] <= l[i+1] for i in range(len(l)-1))


def test_k():
    """
      Tests the different merge sort implementations, the first four fields in
      each list of integers are :
      [0] -> test_type
      [1] -> function name

    """
    ret = [
        ["merge_b_random"],
        ["merge_l_random"],
        ["merge_b_sorted"],
        ["merge_l_sorted"],
        ["merge_b_almost_sorted"],
        ["merge_l_almost_sorted"],
        ["k"]
    ]
    n = 2*10**4
    vals = list(numpy.random.randint(0, n, n))
    vals_sorted = sorted(vals)
    vals_almost_sorted = vals_sorted[:len(vals_sorted)//2]+vals[len(vals)//2::-1]
    for i in range(1,3000,10):
        if is_sorted(vals):
            vals = list(numpy.random.randint(0, n, n))
        print(f"k test : Running tests for k = {i}",end = '\r')
        # Testing merge sort with b sort
        t1 = time.time()
        merge_sort_l(vals, i)
        t2 = time.time()
        ret[0].append(t2-t1)
        ret[6].append(i)
    
    df = pd.DataFrame(ret)
    df.to_csv('k_test.csv', index=False)

    return ret


def test_big_boy(k_1, k_2):
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
        merge_sort_l(vals,n, k_1)
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
    print("Done with test_big_boy")
    df = pd.DataFrame(ret)
    df.to_csv('big_boy.csv', index=False)
    return ret


def medium_sorted_case(k_1, k_2):
    ret = [
        ["merge_l"],
        ["merge_b"],
        ["merge"],
        ["n"]
    ]

    for n in range(10**5, 10**6+1, 5*10**4):
        vals = list(range(0, n))
        vals[n//2:] = vals[n//2-1::-1] 
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
    df.to_csv('med_sort.csv', index=False)
    print("Done with medium_sorted_case")
    return ret


def test_big_random_case(k_1, k_2):
    ret = [
        ["merge_l"],
        ["merge_b"],
        ["merge"],
        ["n"]
    ]

    for n in range(10**5, 2*10**6, 2*10**5):
        vals = list(numpy.random.randint(0, n, n))
        # Testing merge sort with insertion sort
        t1 = time.time()
        merge_sort_l(vals, k_1)
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
    df.to_csv('random.csv', index=False)
    print("Done with test_big_random_case")
    return ret


def test_best_case(k_1, k_2):
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
    df.to_csv('small_boy.csv', index=False)
    print("Done with test_best_case")
    return ret


def progress(percent: int):
    percent = int(percent)
    print(f"[{'='*percent}{' '*(100-percent)}] {percent}%", end='\r')


def test_best_case_insert():
    ret = [
        ["b_sort"],
        ["insertion"],
        ["merge"],
        ["n"]
    ]
    for n in range(1,2*10**4+1,500):
        print(f"Testing best for {n}", end='\r')
        nums = list(range(0,n))
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
    df.to_csv('best_case_only_insert.csv', index=False)
    print("Done with test_best_case")
    return ret

def test_medium_case_insert():
    ret = [
        ["b_sort"],
        ["insertion"],
        ["merge"],
        ["n"]
    ]
    for n in range(1,2*10**4+1,500):
        print(f"testing medium for {n}",end = '\r')
        nums = list(range(0,n))
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
def test_big_case_insert():
    ret = [
        ["b_sort"],
        ["insertion"],
        ["merge"],
        ["n"]
    ]
    for n in range(1,2*10**4+1,500):
        print(f"testing random for {n}", end = '\r')
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
    df.to_csv('test_big_case_insert.csv', index=False)
    print("Done with test_big_case_insert")
    return ret



if __name__ == "__main__":
    print("Started the tests")
    print("asserting that the functions work")
    print(is_sorted(merge_sort(list(range(0, 10)))))
    print(is_sorted(merge_sort_l(list(range(0, 10)),10, 3)))
    print(is_sorted(merge_sort_b(list(range(0, 10)), 3)))
    # print(test_merge_sort(n_range=(1000, 30000), n_step=5000,
    #                      k_range=(1, 100), k_step=1))
    #print(test_best_case_insert())
    #print(test_medium_case_insert())
    #print(test_big_case_insert())
    #print("bruh")


    k = test_k()
    #print("bruh")
    k_1,k_2 = 70,380#k[2][1:][k[0][1:].index(min(k[0][1:]))],k[2][1:][k[1][1:].index(min(k[1][1:]))]
    #print(f"\n\nk for merge_l is {k_1}\nk for merge_b is {k_2}\n\n")
    #print("Testing best case")
    #test_best_case(k_1,k_2)
    #print("Testing worst case")
    #test_big_boy(k_1,k_2)
    print("Testing semi sorted")
    #medium_sorted_case(k_1,k_2)
    #print("Testing big random")
    #test_big_random_case(k_1,k_2)
