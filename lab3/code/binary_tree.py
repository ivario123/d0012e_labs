


class binary_tree_node:
    def __init__(self, value: int = None, number_of_children: list = None, parent=None, left=None, right=None) -> None:
        self.value = value
        self.number_of_children = [0, 0, 0]
        self.parent = parent
        self.right = right
        self.left = left
    """
      Update a nodes child counter, should be called for entier anscestry after a insertion
    """

    def update_child_counter(self):
        if self.right:
            self.number_of_children[1] = self.right.number_of_children[2]+1
        else:
            self.number_of_children[1] = 0
        if self.left:
            self.number_of_children[0] = self.left.number_of_children[2]+1
        else:
            self.number_of_children[0] = 0
        self.number_of_children[2] = self.number_of_children[1] + \
            self.number_of_children[0]
        return
    """
      Checks if a tree is unbalanced, returns 1 if unbalanced 0 if not
    """

    def unbalanced(self, c):
        if abs(self.number_of_children[1] - self.number_of_children[0]) <= 1:
            """
              This captures the unbalanceable case where left side has 1 element and right side has 0
            """
            return 0
        if self.number_of_children[0] > c*self.number_of_children[2]:
            return -1
        if self.number_of_children[1] > c*self.number_of_children[2]:
            return 1
        return 0

    def in_order_walk(self):
        if self.left:
            ret = self.left.in_order_walk()
        else:
            ret = []
        ret.append(self.value)
        if self.right:
            ret.extend(self.right.in_order_walk())
        return ret

    """
      Only used to validate that large trees are balanced too
    """

    def is_valid(self, c):
        ret = self.unbalanced(c) == 0
        if self.left:
            ret = ret == self.left.is_valid(c) == True
        if self.right:
            ret = ret == self.right.is_valid(c) == True
        return ret
    
    def search(self,value):
      if self.value == value:
        return self
      if value > self.value:
        if self.right:
          return self.right.search(value)
        return None
      if self.left:
        return self.left.search(value)
      return None
    
    def find_extreme(self):
        if self == None:
          print("Bruh")
        if self.left == self.right == None:
            return self, 0
        left_best, left_depth, right_best, right_depth = None, 0, None, 0
        if self.left!=None:
            left_best, left_depth = self.left.find_extreme()
        if self.right!=None:
            right_best, right_depth = self.right.find_extreme()
        if not left_best or not right_best:
          if left_best:
            return left_best,left_depth+1
          else:
            return right_best,right_depth+1
        if left_depth > right_depth:
            best = left_best
            best_depth = left_depth+1
        else:
            best = right_best
            best_depth = right_depth+1
        return best, best_depth

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
            # line = f"0,0,{self.value}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f"{self.value}"
            # s = f"{self.number_of_children[0]},{self.number_of_children[1]},{self.value}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f"{self.value}"
            # s = f"{self.number_of_children[0]},{self.number_of_children[1]},{self.value}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f"{self.value}"
        # s = f"{self.number_of_children[0]},{self.number_of_children[1]},{self.value}"
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


class binary_tree:
    def __init__(self, c, root: binary_tree_node = None) -> None:
        self.root = root
        self.c = c
        self.displaying = False
        self.uses_balance = True

    def insert(self, value):
        # If the tree is empty insert a new node at the root
        if not self.root:
            self.root = binary_tree_node(value)
            return
        # Otherwise start looking at
        current_node = self.root
        # Find where to insert the new node
        while 1:
            if value > current_node.value:
                if not current_node.right:
                    break
                current_node = current_node.right
            else:
                if not current_node.left:
                    break
                current_node = current_node.left
        # Insert the new node
        node = binary_tree_node(value, parent=current_node)
        if value > current_node.value:
            current_node.right = node
        else:
            current_node.left = node

        if self.uses_balance:
            node.update_child_counter()
            while current_node:
                current_node.update_child_counter()
                current_node = current_node.parent

            node = self.root
            # Costs worst case O(nlogn)
            self.itterative_rebalance_check(node, value)

    def insert_list(self, L: list):
        for el in L:
            self.insert(el)

    def itterative_rebalance_check(self, node, value):
        while node:
            if node.unbalanced(self.c):
                if self.displaying:
                    print("*"*100)
                    node.display()
                # Balance that node
                # O (n) since sorting is O(n) and the insertion is O(n) and each one is done one time, O(2n) = O(n)
                new_node = binary_tree.rebalance_tree(self.c, node)

                # Overwrite anscetry
                if not node.parent:
                    self.root = new_node
                else:
                    if new_node.value > node.parent.value:
                        node.parent.right = new_node
                    else:
                        node.parent.left = new_node
                node = new_node
                if self.displaying:
                    node.display()
                    print("#"*100)
                return

            # Move down the tree if no unsorted node is found, maximum number of times is h
            if value > node.value:
                node = node.right
            else:
                node = node.left

    def search(self, value):
        return self.root.search(value)

    def is_valid(self):
        return self.root.is_valid(self.c)

    def in_order_walk(self):
        return self.root.in_order_walk()

    def rebalance_tree(c, node, return_type="node"):
        """
            Balances a BST using insertion of a balanced binary search tree
        """
        arr = node.in_order_walk()
        new_root = binary_tree.sorted_array_to_bst(arr)
        tree = binary_tree(c, new_root)
        tree.root.parent = node.parent
        if return_type == "node":
            return tree.root
        return tree

    def sorted_array_to_bst(arr):

        if not arr:
            return None
        mid = (len(arr)) // 2
        root = binary_tree_node(arr[mid])
        root.left = binary_tree.sorted_array_to_bst(
            arr[:mid])
        root.right = binary_tree.sorted_array_to_bst(
            arr[mid+1:])
        root.update_child_counter()
        if root.right != None:
            root.right.parent = root
        if root.left != None:
            root.left.parent = root
        return root

    def display(self):
        if self.root:
            self.root.display()



