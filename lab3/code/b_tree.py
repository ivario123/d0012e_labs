class tree_node:
    def __init__(self, value, parent=None, right=None, left=None):
        self.value = value
        self.parent = parent
        self.right = right
        self.left = left

    def insert_value(self, value):
        # Check if we should go right
        if self.value < value:
            # Check if we have a right child
            if self.right != None:
                self.right.insert_value(value)
            else:
                self.right = tree_node(value, parent=self)
        else:
            if self.left != None:
                self.left.insert_value(value)
            else:
                self.left = tree_node(value, parent=self)
        # Here we should check if we need to rotate the tree
        # ...
        # ...
        # ...
        return

    def layer(self):
        """
          Worstcase O(log(n)) assuming a balanced tree
        """
        if self.parent == None:
            return 0
        return self.parent.layer()+1

    def rotate_left(self):
          # Keep the useful data
          left = self.left
          parent = self.parent
          current = self
          right = self.right


          # Rotate the tree
          right.parent = self.parent    # Change parent nodes
          current.parent = right        # ...
          current.right = right.left    # Set the new left sides right side to the old right sides left side
          right.left = current          # Set the new right sides left side to the old top

          # Check if we have a parent node
          if self.parent != None:
            # Check wich side of the parent we are on
            if self.parent.value < self.value:
              self.parent.right = right
            else:
              self.parent.left = right

          
          return right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f"{self.value}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f"{self.value}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f"{self.value}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f"{self.value}"
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




import numpy as np

if __name__ == "__main__":
  root = tree_node(0)
  root.insert_value(1)
  root.insert_value(2)
  root.insert_value(3)
  root.insert_value(-2)
  root.insert_value(-1)
  root.display()
  root.rotate_left()
  root.display()