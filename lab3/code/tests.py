from numpy.lib.function_base import average
from  binary_tree import *
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import os
from optparse import OptionParser
import inspect
class tests:
    def __init__(self, input_data: list = list(np.random.randint(-100, 100, 60)), c_range: list = [0.51, 1.0], c_interval: int = 0.01, length_range=[10**3, 5*10**4], length_interval=2*10**3):
        self.input_data = input_data
        self.c_range = c_range
        self.c_interval = c_interval
        self.results = {"validate_functions": [], "constant_c_varying_length": [], "lengths_tested": [
        ], "constant_length_varying_c": [], "c_values_tested": [], "normal_bst": [], "length_tested_bst": [],
        "unbalanced_search_time":[],"balanced_search_time":[]}
        self.length_range = length_range
        self.length_interval = length_interval
        return
    def show_for_average_c(self):
      print("...___...___"*(100//12))
      print(self.input_data)
      c = self.c_range[0]+self.c_range[1]
      c/=2
      tree = binary_tree(c)
      tree.displaying = True
      tree.insert_list(self.input_data)
      tree.display()
      if tree.is_valid():
        print("The final tree is valid")
      else: 
        print("The final tree is not valid")
      print(tree.root.number_of_children,c*tree.root.number_of_children[2])
    def plot(self, x: list, y: list, x_label: str, y_label: str, plot_header: str,labels: list = None):
        fig = plt.figure()
        plt.title(plot_header, fontsize='16')

        if type(y[0]) == list:
          plt.plot(x,y[0],label =labels[0])
          plt.plot(x,y[1],label=labels[1])
        else:
          plt.plot(x, y, label="")
        plt.legend(loc="upper right")
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid()
        # Figures out the absolute path for you in case your working directory moves around.
        my_path = os.path.dirname(os.path.abspath(__file__))
        fig.savefig(my_path + f"/plots/{plot_header.replace(' ','_')}.png")

    def test_normal_bst(self):
        print("*"*100)
        print("Testing a normal bst with varying input length")
        for length in range(self.length_range[0], self.length_range[1], self.length_interval):
            print(f"Testing for a normal BST with input length {length}")
            tree = standard_bst()
            tree.uses_balance = False
            data = list(np.random.randint(-length, length, length))
            time_1 = time.time()
            tree.insert_list(data)
            time_2 = time.time()
            self.results["normal_bst"].append(time_2-time_1)
            self.results["length_tested_bst"].append(length)

        x = list(self.results["length_tested_bst"])
        y = list(self.results["normal_bst"])
        self.plot(x, y,
                  "Input_length", "Execution time [s]", f"Execution time as a function of input length for a standard bst ")
    """
    def test_compare_search(self):
        print(
            f"Comparing search time between normal bst and balanced bst\nUsing length = {self.length_range[1]//2}")
        data = list(
            np.random.randint(-self.length_range[1], self.length_range[1], self.length_range[1]//2))
        tree_not_balanced = binary_tree(0)
        tree_not_balanced.uses_balance = False
        tree_not_balanced.insert_list(data)
        if self.results["c_values_tested"] == []:
          log_c = True
        else:
          log_c = False
        num_to_find = tree_not_balanced.root.find_extreme()[0]
        print(f"Number to find {num_to_find.value}")
        for c in list(np.arange(self.c_range[0], self.c_range[1], self.c_interval)):
            print(f"Running test for c = {c}")
            tree_balanced = binary_tree(c)
            tree_balanced.insert_list(data)
            time_1_balanced = time.time()
            tree_balanced.search(num_to_find.value)
            time_2_balanced = time.time()
            tree_not_balanced.search(num_to_find.value)
            time_unbalanced = time.time()
            self.results["balanced_search_time"].append(time_2_balanced-time_1_balanced)
            self.results["unbalanced_search_time"].append(time_unbalanced-time_2_balanced)
            if log_c:
              self.results["c_values_tested"].append(c)
            
        
        x = list(self.results["c_values_tested"])
        y = [self.results["balanced_search_time"],self.results["unbalanced_search_time"]]
        self.plot(x, y,
                  "c value", "Execution time [s]", f"Search time for a balanced bst as a function of unbalance ")
    """

    def validate_functions(self):
        """
          Verifies that the functions work for a c in the range
        """
        print("*"*100)
        print("Validating that the functions still produce a valid result")
        tree = binary_tree(self.c_range[0])
        tree.displaying = True
        tree.insert_list(self.input_data)
        return tree.root.is_valid(self.c_range[0])

    def test_preorderd_list(self):
      print("*"*100)
      print("Testing preorder list")
      print("*"*100)
      results_sorting = []
      results_not_sorting = []
      length = self.length_range[0]
      data = list(np.random.randint(-length, length, length))
      data = sorted(data)
      countLoops = 0
      for c in list(np.arange(self.c_range[0], self.c_range[1], self.c_interval)):
        print(f"Testing for c = {c}")
        tree = binary_tree(c)
        time_1 = time.time()
        tree.insert_list(data)
        time_2 = time.time()
        results_sorting.append(time_2-time_1)
        tree = standard_bst()
        time_1 = time.time()
        tree.insert_list(data)
        time_2 = time.time()
        results_not_sorting.append(time_2-time_1)
        countLoops = countLoops+1
      x = list(np.arange(self.c_range[0], self.c_range[1], self.c_interval))
      y = [results_sorting, results_not_sorting]
      self.plot(x, y,
                "c value", "Execution time [s]", f"Execution time as a function of c for a preorderd list",labels=["Sorted","Not sorted"])
    def test_semi_sorted_list(self):
      print("*"*100)
      print("Testing semi sorted list")
      print("*"*100)
      results_sorting = []
      results_not_sorting = []
      length = self.length_range[0]
      data = sorted(list(np.random.randint(-length, length, length)))
      data = data[len(data)//2:]+data[:len(data)//2]
      countLoops = 0
      for c in list(np.arange(self.c_range[0], self.c_range[1], self.c_interval)):
        print(f"Testing for c = {c}")
        tree = binary_tree(c)
        time_1 = time.time()
        tree.insert_list(data)
        time_2 = time.time()
        results_sorting.append(time_2-time_1)
        tree = standard_bst()
        time_1 = time.time()
        tree.insert_list(data)
        time_2 = time.time()
        results_not_sorting.append(time_2-time_1)
        countLoops = countLoops+1
      x = list(np.arange(self.c_range[0], self.c_range[1], self.c_interval))
      y = [results_sorting, results_not_sorting]
      self.plot(x, y,
                "c value", "Execution time [s]", f"Execution time as a function of c for a semi sorted list",labels=["Sorted","Not sorted"])
    def test_reverse_sorted_list(self):
      print("*"*100)
      print("Testing reverse sorted list")
      print("*"*100)
      results_sorting = []
      results_not_sorting = []
      length = self.length_range[0]
      data = sorted(list(np.random.randint(-length, length, length)))
      data = data[::-1]
      countLoops = 0
      for c in list(np.arange(self.c_range[0], self.c_range[1], self.c_interval)):
        print(f"Testing for c = {c}")
        tree = binary_tree(c)
        time_1 = time.time()
        tree.insert_list(data)
        time_2 = time.time()
        results_sorting.append(time_2-time_1)
        tree = standard_bst()
        time_1 = time.time()
        tree.insert_list(data)
        time_2 = time.time()
        results_not_sorting.append(time_2-time_1)
        countLoops = countLoops+1
      x = list(np.arange(self.c_range[0], self.c_range[1], self.c_interval))
      y = [results_sorting, results_not_sorting]
      self.plot(x, y,
                "c value", "Execution time [s]", f"Execution time as a function of c for a reverse sorted list",labels=["Sorted","Not sorted"])
    def test_random_list(self):
      print("*"*100)
      print("Testing random list")
      print("*"*100)
      results_sorting = []
      results_not_sorting = []
      length = self.length_range[0]
      data = sorted(list(np.random.randint(-length, length, length)))
      countLoops = 0
      for c in list(np.arange(self.c_range[0], self.c_range[1], self.c_interval)):
        print(f"Testing for c = {c}")
        tree = binary_tree(c)
        time_1 = time.time()
        tree.insert_list(data)
        time_2 = time.time()
        results_sorting.append(time_2-time_1)
        tree = standard_bst()
        time_1 = time.time()
        tree.insert_list(data)
        time_2 = time.time()
        results_not_sorting.append(time_2-time_1)
        countLoops = countLoops+1
      x = list(np.arange(self.c_range[0], self.c_range[1], self.c_interval))
      y = [results_sorting, results_not_sorting]
      self.plot(x, y,
                "c value", "Execution time [s]", f"Execution time as a function of c for a random list",labels=["Sorted","Not sorted"])
    def test_constant_c_varying_length(self):
        print("*"*100)
        c = self.c_range[1]+self.c_range[0]
        c /= 2
        print("Running the tests for constant_c_varying_length")
        for length in range(self.length_range[0], self.length_range[1], self.length_interval):
            print(f"Testing with c = {c} for length = {length} ")
            self.input_data = list(np.random.randint(-length, length, length))
            tree = binary_tree(c)
            time_1 = time.time()
            tree.insert_list(self.input_data)
            time_2 = time.time()
            self.results["constant_c_varying_length"].append(time_2-time_1)
            self.results["lengths_tested"].append(length)
            print(f"Run took {time_2-time_1} s")
            print("- - "*25)
        x = list(self.results["lengths_tested"])
        y = list(self.results["constant_c_varying_length"])
        self.plot(x, y,
                  "Input_length", "Execution time [s]", f"Execution time as a function of input length for c = {(self.c_range[1]+self.c_range[0])/2} ")
    def run_all_tests(self):
        functions = inspect.getmembers(self, predicate=inspect.ismethod)
        for key, value in functions:
            if 'test' in key and key != "run_all_tests":
                value()
        test.dump_to_csv("latest_run")
    
    def dump_to_csv(self, csv_name):
        df = [pd.DataFrame({k: v}) for k, v in self.results.items()]

        df = pd.concat(df, axis=0)
        print(df)
        #df = pd.DataFrame.from_dict(self.results)
        file_dir = os.path.dirname(os.path.abspath(__file__))
        csv_folder = 'csv_files'
        file_path = os.path.join(file_dir, csv_folder, f'{csv_name}.csv')
        df.to_csv(file_path, header=False, index=False)
        pass


if __name__ == "__main__":
    test = tests()
    test.c_interval = 0.01
    test.length_range[0] = 10**4
    valid = test.validate_functions()
    assert valid
    print("Still works")
    c = 0.8
    test.c_range[0] = c
    test.c_range[1] = c
    test.show_for_average_c()
    
    #test.test_semi_sorted_list()
    #test.run_all_tests()
    print(test.results)
    #test.show_for_average_c()