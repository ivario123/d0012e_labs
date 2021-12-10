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
    def delete_key(self,key):
        """
            Really naive way to delete element from list
        """
        root = self.search(key)
        arr = root.in_order_walk()
        arr.remove(key)
        new_root, bruh = tree_node.sorted_array_to_bst(arr)
        root.key = new_root.key
        root.right = new_root.right
        root.left = new_root.left
        if root.left and root.left.left:
            root.left.left.parent = root
        if root.right and root.right.right:
            root.right.right.parent = root
        return
    def insert_key(self, key):
        # O(n)
        parent = self.search(key)
        #if key == parent.key:
            # Recounting nodes
        #    parent.added_child()
            # If we need to rebalance we will
        #    parent.needs_balancing()
        #    print("Duplicate found")
        #    return
        # Insert the node below the parent
        node = tree_node(key, parent=parent, sort_method=parent.sort_method,
                         sorting_threshold=parent.sorting_threshold)
        if key > parent.key:
            parent.right = node
        else:
            parent.left = node
        # The following two function calls could be merged into one
        # Recounting nodes and sorting if needed O(h*h) in worst case
        node.added_child()
        node.needs_balancing()

        return

    def threshold_check(self):
        """
            Checks if a node needs to be balanced
        """
        if abs(self.children_right-self.children_left) <= 1:
            return None
        balance = None
        sum_children = self.children_right+self.children_left
        if self.sort_method == "absolute":
            balance = self.get_balance()
        else:
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

    def rotate_left(self):
        """
            Rotates a BST to the left around the root self
        """
        if self.right == None:
            return
        # Temporary storage variables
        current = {"key": self.key, "left": self.left,
                   "children_left": self.children_left}
        el = self.right
        right = {"key": el.key, "right": el.right, "left": el.left,
                 "children_left": el.children_left, "children_right": el.children_right}

        rotation_data = {"right_left": self.right.left}
        # Overwrite the top element
        self.key = right["key"]
        # Check if we have to reoder the parent pointers
        if self.right.right != None:
            self.right.right.parent = self              # Pop from the right side
            # move the right pointer one index down
            self.right = right["right"]
        else:
            self.right = None
        # Adding a new left node
        self.left = tree_node(current["key"], parent=self, right=rotation_data["right_left"], left=current["left"],
                              sorting_threshold=self.sorting_threshold, sort_method=self.sort_method)
        # Reoder parent pointers if needed
        if self.left.right:
            self.left.right.parent = self.left
        if self.left.left:
            self.left.left.parent = self.left
        # Reoder child counters
        self.left.children_left = current["children_left"]
        self.left.children_right = right["children_left"]
        self.children_left = right["children_left"]+current["children_left"]+1
        self.children_right = right["children_right"]

        return

    def rotate_right(self):
        """
            Rotates a BST to the right around the root self
        """
        if self.left == None:
            return
        # Temporary storage variables

        current = {"key": self.key, "left": self.left,
                   "children_right": self.children_right}
        el = self.left
        if el:
            left = {"key": el.key, "right": el.right, "left": el.left,
                    "children_left": el.children_left, "children_right": el.children_right}
        rotation_data = {"left_right": self.left.right}

        # Overwrite the top key
        self.key = self.left.key
        if self.left.left != None:
            self.left.left.parent = self              # Pop from the left side
            self.left = self.left.left               # move the right pointer one index down
        else:
            self.left = None
        # Owerwrite the right node
        self.right = tree_node(current["key"], parent=self, left=rotation_data["left_right"], right=self.right,
                               sorting_threshold=self.sorting_threshold, sort_method=self.sort_method)
        # Overwrite the parent pointers if needed
        if self.right.right:
            self.right.right.parent = self.right
        if self.right.left:
            self.right.left.parent = self.right
        # Log the new child values
        self.right.children_right = current["children_right"]
        self.right.children_left = left["children_right"]
        self.children_right = current["children_right"] + \
            left["children_right"]+1
        self.children_left = left["children_left"]

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

        if self.parent and self.key < self.parent.key:
            print('-'*100)
            self.parent.display()
            self.parent.children_left = self.children_left+self.children_right+1
            self.parent.display()
            print('-'*100)
        elif self.parent:
            print('-'*100)
            self.parent.display()
            self.parent.children_right = self.children_right+self.children_left+1
            self.parent.display()
            print('-'*100)
        return

    def sorted_array_to_bst(arr):

        if not arr:
            return None,0

        # find middle
        mid = (len(arr)) // 2

        # make the middle element the root
        root = tree_node(arr[mid], sort_method="insertion")

        # left subtree of root has all
        # values <arr[mid]
        root.left, root.children_left = tree_node.sorted_array_to_bst(
            arr[:mid])

        # right subtree of root has all
        # values >arr[mid]
        root.right, root.children_right = tree_node.sorted_array_to_bst(
            arr[mid+1:])
        if root.right !=None:
            root.right.parent = root
        if root.left!=None:
            root.left.parent = root
        #root.children_left+=1
        #root.children_right+=1
        return root, root.children_left+root.children_right+1

        return

    """
        Balancing helper functions
    """

    def needs_balancing(self,check_parent = True):
        """Checks if a tree needs to be rebalanced, by using the types sort_method variable.
            I think that this works tho.
        """
        # This should work.
        presorted = False
        if self.parent and check_parent:
            presorted = self.parent.needs_balancing()
        if not presorted:
            balance = self.threshold_check()
            if balance:
                print("*"*100)
                #main_root.display()
                self.display()
                if self.sort_method == "rotation":
                    self.balance_rotation()
                else:
                    self.balance_insert()
                self.display()
                print("*"*100)
                presorted = True

        return sorted

    def balance_rotation(self):
        """
            Balance through rotation
            This one might miss a case, don't think so but it seems like it for unbalanced lists. 
            We might have to itterate down the list for very unbalanced lists. So sorting from the base up.
        """
        balancing_factor = self.get_balance()
        if balancing_factor >= -1 and balancing_factor <= 1:
            return
        if balancing_factor <= -1:
            if self.left != None and not self.left.get_balance() < 0:
                self.left.rotate_left()
            self.rotate_right()
        else:
            if self.right != None and not self.right.get_balance() > 0:
                self.right.rotate_right()
            self.rotate_left()
        return

    def get_balance(self):
        """
            Get how unblanced a tree is
        """
        if self.children_right == 0 == self.children_left:
            return 0
        elif self.children_right == 0:
            return-self.children_left
        elif self.children_left == 0:
            return self.children_right
        else:
            return self.children_right - self.children_left
    """
        Recount the number of children that a parent has
    """

    def added_child(self):
        """
          Recounts the number of children that a parent node has.
          Only needs to be called after a new node has been added
          ### Complexity O(h) where h is the number of nodes between the current node and the root.
        """

        if self.left is not None:
            self.children_left = self.left.children_left + self.left.children_right+1
        else:
            self.children_left = 0
        if self.right is not None:
            self.children_right = self.right.children_right + self.right.children_left+1
        else:
            self.children_right = 0
        if self.parent != None:
            self.parent.added_child()
        if self.parent == None:
            print("found the root")
        return
    """
        Helper functions, to check the number of nodes under or over a node
    """

    def get_nodes(self):
        """
            Returns the number of nodes under this root.
        """
        if self.left == None:
            ret = 0
        else:
            ret = self.left.get_nodes()
        if self.right != None:
            ret += self.right.get_nodes()
        return ret+1

    def is_valid(self):
        """
            returns wether a tree is valid or not
        """
        sum_children = self.children_left+self.children_right
        if sum_children < 2:
            return True
        ret = self.children_left <= c*sum_children and self.children_right <= c*sum_children
        if self.left != None:
            ret = ret == self.left.get_nodes() == True or sum_children <= 2
        if self.right != None:
            ret = ret == self.right.get_nodes() == True or sum_children <= 2
        return ret

    def layer(self):
        """
          Worstcase O(log(n)) assuming a balanced tree
        """
        if self.parent == None:
            return 0
        return self.parent.layer()+1
    """
        Search and to sorted list functions
    """

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

    def in_list(self, key):
        """
          Checks if a key is in the tree
          # Complexity O(h) where h is the height of the tree
          # Returns 1 if in list -1 in all other cases 
        """
        if self.key != key:
            if key > self.key:
                if self.right != None:
                    return self.right.in_list(key)
                return False
            else:
                if self.left != None:
                    return self.left.in_list(key)
                return False
        return True

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
            if self.parent:
               line = f"{self.children_left},{self.children_right},{self.key},{self.parent.key}"
            else:
               line = f"{self.children_left},{self.children_right},{self.key}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            # s = f"{self.key}"
            if self.parent:
               s = f"{self.children_left},{self.children_right},{self.key},{self.parent.key}"
            else:
               s= f"{self.children_left},{self.children_right},{self.key}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            # s = f"{self.key}"
            if self.parent:
               s = f"{self.children_left},{self.children_right},{self.key},{self.parent.key}"
            else:
               s = f"{self.children_left},{self.children_right},{self.key}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        # s = f"{self.key}"
        if self.parent:
           s = f"{self.children_left},{self.children_right},{self.key},{self.parent.key}"
        else:
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

c = .65
counter = 0
main_root = None
if __name__ == "__main__":
    nums = list(np.random.randint(-100, 100, 10))
    main_root = tree_node(nums[0],sort_method="insertion")

    for el in nums[1:]:
        main_root.insert_key(el)
    _sorted = main_root.in_order_walk()
    main_root.display()
    print(len(_sorted),len(nums))
    print(main_root.children_left, main_root.children_right,main_root.children_right+main_root.children_left+1,
          c*(main_root.children_right+main_root.children_left))
    if(len(_sorted) != main_root.children_right+main_root.children_left+1):
        print(nums)
    if main_root.is_valid():
        print("this shit worked")
    else:
        print("Still a strong nope")
    if sorted(_sorted) == _sorted:
        print("In order walk works")
    else:
        print("In order walk is wack")

    if _sorted != sorted(nums):
        print("Something went wrong, check log")
