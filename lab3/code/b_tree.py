import numpy as np
c = .5
counter = 0


class tree_node:
    def __init__(self, value, parent=None, right=None, left=None):
        self.value = value
        self.parent = parent
        self.right = right
        self.left = left
        self.children_left = 0
        self.children_right = 0

    def insert_value(self, value):
        """
          Inserts a node in the tree.
          Isertion operation has complexity of O(h) where h is the number of levels in the tree.
          However since we also sort it we have the timeximplexity of O(k*n) which still is O(n).
        """
        if self.value == value:
         print("Duplicates")
         return self
        # Inserting the value in the tree
        parent = self.search(value)   # Get the index
        node = tree_node(value, parent)
        if value > parent.value:
            parent.right = node
        else:
            parent.left = node
        parent.added_child()      # Recount the number of children for every node

        root = node.needs_balancing()
        return root

    def needs_balancing(self):
        """Returns the root node, expects a leaf"""
            # Base case is we are at the root
        if self.parent == None:
            return self

        # If we are not at the root, go to the next level
        root = self.parent.needs_balancing()
        # This should work.
        # sum_children = self.children_right+self.children_left
        # balance = self.children_right > c*sum_children or self.children_right > (1-c)*sum_children
        # This works
        balance = self.get_balance()
        if balance:         # If we need to balance the tree, do so.
          print('*'*100)
          self.display()
          print(balance)
          self.balance()
        return root


    def balance(self):
        bf = self.get_balance()
        if bf < 2 and bf > -2: 
            return self
        if bf < -1:
            if self.left.get_balance() < 0:
                new_root = self.rotate_right()
            else:
                self.left = self.left.rotate_left()
                new_root = self.rotate_right()
        else:
            if self.right.get_balance() > 0:
                new_root = self.rotate_left()
            else:
                self.right = self.right.rotate_right()
                new_root = self.rotate_left()
        return new_root
        # if balance > 0:
        #     if self.right != None and self.right.get_balance() == -1:
        #         self.right = self.right.rotate_right()
        #         self.display()
        #     self = self.rotate_left()
        # else :
        #     if self.left != None and self.left.get_balance() == 1:
        #         self.left = self.left.rotate_left()
        #         self.display()
        #     self = self.rotate_right()
        # self.display()

    def get_balance(self):
        if self.children_right== 0 == self.children_left:
            return 0
        elif self.children_right == 0:
            return-self.children_left
        elif self.children_left == 0:
            return self.children_right
        else:
            return self.children_right - self.children_left
        # sum_children = self.children_left+self.children_right
        # if sum_children == 0:
        #     return 0
        # if self.children_left > (1-c)*sum_children:
        #     return -1
        # if self.children_right > c*sum_children:
        #     return 1
        # return 0

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
        #if self.get_balance():
        #  self.needs_balancing()
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


"""
      Test section

"""


if __name__ == "__main__":
    root = tree_node(0)

    root.display()

    nums = list(np.random.randint(-100, 100, 2**4))
    for el in nums:
        root = root.insert_value(el)
    root.display()
    print(f"Something fucked up : {root.in_list(0)==False}")
    _sorted = root.in_order_walk()
    if sorted(_sorted) == _sorted:
      print("In order walk works")
    else:
      print("In order walk is wack") 
    print(_sorted)
