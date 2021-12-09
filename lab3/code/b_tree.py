import numpy as np


class tree_node:
    def __init__(self, value, parent=None, right=None, left=None, sort_method="rotation", sorting_threshold="absolute"):
        self.value = value
        self.parent = parent
        self.right = right
        self.left = left
        self.children_left = 0
        self.children_right = 0
        self.sort_method = sort_method
        self.sorting_threshold = sorting_threshold

    def insert_value(self, value):
        """
          Inserts a node in the tree.
          Isertion operation has complexity of O(h) where h is the number of levels in the tree.
          However since we also sort it we have the timeximplexity of O(k*n) which still is O(n).
        """
        parent = self.search(value)   # Get the index
        if parent.value == value:
            print("Duplicates")
            node = self
        else:
            # Inserting the value in the tree
            node = tree_node(
                value, parent, sorting_threshold=self.sorting_threshold, sort_method=self.sort_method)
            if value > parent.value:
                parent.right = node
            else:
                parent.left = node
            parent.added_child()      # Recount the number of children for every node

        root = node.needs_balancing()
        return root

    def needs_balancing(self):
        """Returns the root node, expects a leaf"""
        root = self.parent ==  None
        balance = 0
        # This should work.
        if self.sort_method == "absolute":
            balance = self.get_balance()
        else:
            sum_children = self.children_right+self.children_left
            if self.children_left and self.children_left > c*sum_children:
                balance = 1
            elif self.children_right and self.children_right > (1-c)*sum_children:
                balance = -1
            else:
                balance = 0

        #
        # This works
        if balance:         # If we need to balance the tree, do so.
            print('*'*100)
            self.display()
            nodes_before = self.get_nodes()
            print(balance)
            if self.sort_method == "rotation":
                self = self.balance_rotation()
            elif self.sort_method == "insert":
                new_node = self.balance_insert()
                self = new_node
            self.display()
            nodes_after = self.get_nodes()
            if(nodes_before != nodes_after):
                print("wtf")

        # Base case is we are at the root
        if root:
            return self

        # If we are not at the root, go to the next level
        root = self.parent.needs_balancing()
        return root

    def balance_insert(self,start = None,end = None,orderd= None):

        if orderd == None:
          orderd = self.in_order_walk()
          print(orderd)
          start = 0
          end = len(orderd)-1
        if start > end:
          return self
        print(orderd[start:end])
        mid = (start+end)//2
        root = tree_node(orderd[mid],parent=self.parent,sort_method=self.sort_method,sorting_threshold=self.sorting_threshold)
        root.left = root.balance_insert(start,mid-1,orderd)
        root.right = root.balance_insert(mid+1,end,orderd)
        return root
        
        return root

        if start >= end:
          self.value = orderd[start]
          return
        if start != mid:
          self.left = tree_node(0,parent = self,sort_method=self.sort_method,sorting_threshold=self.sorting_threshold)
          self.left.balance_insert(0,mid-1,orderd)
        else:
          self.left = None

        self.value = orderd[(start+end)//2]
        self.right = tree_node(0,parent = self,sort_method=self.sort_method,sorting_threshold=self.sorting_threshold)
        self.right.balance_insert(mid+1,end,orderd)
        return

    def balance_rotation(self):
        balancing_factor = self.get_balance()
        if self.sorting_threshold == "absolute":
            if balancing_factor < 2 and balancing_factor > -2:
                return self
        if balancing_factor < -1:
            if self.left != None and not self.left.get_balance() < 0:
                self.left = self.left.rotate_left()
            new_root = self.rotate_right()
        else:
            if self.right != None and not self.right.get_balance() > 0:
                self.right = self.right.rotate_right()
            new_root = self.rotate_left()
        return new_root

    def get_balance(self):
        if self.children_right == 0 == self.children_left:
            return 0
        elif self.children_right == 0:
            return-self.children_left
        elif self.children_left == 0:
            return self.children_right
        else:
            return self.children_right - self.children_left

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
            self = self.parent.added_child()
        return self

    def get_nodes(self):
        if self.left == None:
            ret = 0
        else:
            ret = self.left.get_nodes()
        if self.right != None:
            ret += self.right.get_nodes()
        return ret+1

    def layer(self):
        """
          Worstcase O(log(n)) assuming a balanced tree
        """
        if self.parent == None:
            return 0
        return self.parent.layer()+1

    def in_order_walk(self):
        """
          Generates an orderd list of elements. Orderd in ascending order
          ### Complexity O(n) since it's a divide and conqure sollution with no other operations
        """
        if self.left == None:
            ret = []
        else:
            ret = self.left.in_order_walk()
        ret.append(self.value)
        if self.right != None:
            ret.extend(self.right.in_order_walk())
        return ret

    def rotate_left(self):
        """
          Rotates a tree to the left around the node (self)
          ### Complexity O(1) since there are no loops or recursions
        """
        # Keep the useful data
        current = self
        if self.right == None:
            return self
        right = self.right

        # Rotate the tree
        right.parent = self.parent    # Change parent nodes
        current.parent = right        # ...
        # Set the new left sides right side to the old right sides left side
        current.right = right.left
        # Change the child counters
        current.children_right = right.children_left
        right.children_left = current.children_left+current.children_right+1

        right.left = current          # Set the new right sides left side to the old top

        # Check if we have a parent node
        if right.parent != None:
            # Check wich side of the parent we are on
            if right.parent.value < right.value:
                right.parent.right = right
            else:
                right.parent.left = right
        return right

    def rotate_right(self):
        """
          Rotates a tree to the right around the node (self)
          ### Complexity O(1) since there are no loops or recursions
        """
        current = self
        if self.left == None:
            return self
        left = self.left

        # Rotate the tree
        left.parent = self.parent    # Change parent nodes
        current.parent = left        # ...
        # Change the child counters
        current.children_left = left.children_right
        left.children_right = left.children_right+current.children_right+1
        # Set the new left sides right side to the old right sides left side
        current.left = left.right
        left.right = current          # Set the new right sides left side to the old top

        # Check if we have a parent node
        if left.parent != None:
            # Check wich side of the parent we are on
            if left.parent.value < left.value:
                left.parent.right = left
            else:
                left.parent.left = left
        return left

    def search(self, key):
        """
          Finds a element of the given value or if no such element exists, returns the parent. This requires a check by the caller
          to verify if it's the parent of the supposed element.
          # Complexity O(h) where h is the height of the tree
          # Return element or it's supposed parent.
        """
        if self.value != key:
            if key > self.value:
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
        if self.value != key:
            if key > self.value:
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
            line = f"{self.value}"
            #line = f"{self.children_left},{self.children_right},{self.value}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f"{self.value}"
            #s = f"{self.children_left},{self.children_right},{self.value}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f"{self.value}"
            #s = f"{self.children_left},{self.children_right},{self.value}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f"{self.value}"
        #s = f"{self.children_left},{self.children_right},{self.value}"
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


c = .5
"""
      Test section

"""


if __name__ == "__main__":
    nums = list(set(list(np.random.randint(-100, 100, 2**4))))
    # Testing for the lab
    #root = tree_node(nums[0], sorting_threshold="c")
    # Testing as an avl tree
    root = tree_node(nums[0])#, sorting_threshold="absolute",sort_method="rotation")

    root.display()

    for el in nums[1:]:
        root = root.insert_value(el)
    root.display()
    _sorted = root.in_order_walk()
    if sorted(_sorted) == _sorted:
        print("In order walk works")
    else:
        print("In order walk is wack")
    print(_sorted)
    print(sorted(nums))
    print(len(_sorted))
    if _sorted != sorted(nums):
      print("Something went wrong, check log")
    print(root.children_left, root.children_right,
          c*(root.children_right+root.children_left))
