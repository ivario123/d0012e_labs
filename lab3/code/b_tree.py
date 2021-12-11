from ctypes import memmove
import numpy as np
from numpy.core.fromnumeric import sort


class tree_node:
    def __init__(self, key, parent=None, right=None, left=None, sort_method="rotation", sorting_threshold="c"):
        self.key = key
        self.parent = parent
        self.right = right
        self.left = left
        self.children_left = 0
        self.children_right = 0
        self.sort_method = sort_method
        self.sorting_threshold = sorting_threshold

    def update_child_counter(self):
        if self.left is not None:
            self.children_left = self.left.children_left + self.left.children_right+1
        else:
            self.children_left = 0
        if self.right is not None:
            self.children_right = self.right.children_right + self.right.children_left+1
        else:
            self.children_right = 0
        return

    def insert_key(self, key):
        # O(h)
        parent = self.search(key)
        node = tree_node(key, parent=parent, sort_method=parent.sort_method,
                         sorting_threshold=parent.sorting_threshold)
        if key > parent.key:
            parent.right = node
        else:
            parent.left = node

        """
            Balance if needed
        """
        el = self
        sorted = False
        while not sorted and (el.right or el.left):
            el.update_child_counter()
            balance = el.threshold_check()
            if balance:
                el.balance_insert()
                self.display()
                sorted = True
            if key < el.key:
                if not el.left:
                    break
                el = el.left
            else:
                if not el.right:
                    break
                el = el.right
        
        if el.parent:
            sum_children = el.children_right+el.children_left+1
            if el.key > el.parent.key:
                el.parent.right = el
                el.parent.children_right = sum_children
            else:
                el.parent.left = el
                el.parent.children_left = sum_children
        print("*"*100)
        self.display()
        el.display()
        print("*"*100)
        return

    def threshold_check(self):
        """
            Checks if a node needs to be balanced
        """
        if abs(self.children_right-self.children_left) <= 1:
            return None
        balance = None
        sum_children = self.children_right+self.children_left

        if sum_children < 2:
            balance = None
        else:
            if self.children_left and self.children_left > c*sum_children:
                balance = -1
            elif self.children_right and self.children_right > (c)*sum_children:
                balance = 1
            else:
                balance = None
        return balance

    def balance_insert(self):
        """
            Balances a BST using insertion of a balanced binary search tree
        """
        arr = self.in_order_walk()
        new_root, bruh = tree_node.sorted_array_to_bst(arr)
        self.key = new_root.key
        self.right = new_root.right
        self.left = new_root.left
        self.children_right = new_root.children_right
        self.children_left = new_root.children_left
        assert self.children_left + self.children_right+1 == bruh
        if self.parent and self.key > self.parent.key:
            self.parent.right = self
        elif self.parent:
            self.parent.left = self
        return

    def sorted_array_to_bst(arr):

        if not arr:
            return None, 0
        mid = (len(arr)) // 2
        root = tree_node(arr[mid], sort_method="insertion")
        root.left, root.children_left = tree_node.sorted_array_to_bst(
            arr[:mid])
        root.right, root.children_right = tree_node.sorted_array_to_bst(
            arr[mid+1:])
        if root.right != None:
            root.right.parent = root
        if root.left != None:
            root.left.parent = root
        return root, root.children_left+root.children_right+1
    """
        Recount the number of children that a parent has
    """

    def added_child(self):
        """
          Recounts the number of children that a parent node has.
          Only needs to be called after a new node has been added
          ### Complexity O(h) where h is the number of nodes between the current node and the root.
        """
        self.update_child_counter()         # Constant time
        if self.parent != None:
            self.parent.added_child()
        return

    def in_order_walk(self):
        """
          Generates an orderd list of elements. Orderd in ascending order
          ### Complexity O(n) since it's a divide and conqure sollution with no other operations
        """
        if self.left == None:
            ret = []
        else:
            ret = self.left.in_order_walk()
        ret.append(self.key)
        if self.right != None:
            ret.extend(self.right.in_order_walk())
        return ret

    def search(self, key):
        """
          Finds a element of the given key or if no such element exists, returns the parent. This requires a check by the caller
          to verify if it's the parent of the supposed element.
          # Complexity O(h) where h is the height of the tree
          # Return element or it's supposed parent.
        """
        if self.key != key:
            if key > self.key:
                if self.right != None:
                    return self.right.search(key)
            else:
                if self.left != None:
                    return self.left.search(key)
        return self

   

    """
      Some display code joinked from stack overflow, modernized a bit but still the same
    """

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            # line = f"{self.key}"
            line = f"0,0,{self.key}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            # s = f"{self.key}"
            s = f"{self.children_left},{self.children_right},{self.key}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            # s = f"{self.key}"
            s = f"0,{self.children_right},{self.key}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        # s = f"{self.key}"
        s = f"{self.children_left},{self.children_right},{self.key}"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


"""
      Test section

"""

c = .5
counter = 0
main_root = None
if __name__ == "__main__":
    nums = list(np.random.randint(-100, 100, 15))
    main_root = tree_node(nums[0], sort_method="insertion")

    for el in nums[1:]:
        main_root.insert_key(el)
    _sorted = main_root.in_order_walk()
    main_root.display()
    print(len(_sorted), len(nums))
    print(main_root.children_left, main_root.children_right, main_root.children_right+main_root.children_left+1,
          c*(main_root.children_right+main_root.children_left))
    if(len(_sorted) != main_root.children_right+main_root.children_left+1):
        print(nums)
    else:
        print("Still a strong nope")
    if sorted(_sorted) == _sorted:
        print("In order walk works")
    else:
        print("In order walk is wack")

    if _sorted != sorted(nums):
        print("Something went wrong, check log")
