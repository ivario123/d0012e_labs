import numpy as np
class binary_tree_node:
    def __init__(self,value:int=None,number_of_children:list = None,parent = None,left = None,right = None) -> None:
        self.value = value
        if number_of_children:
          self.number_of_children = number_of_children
        else:
          self.number_of_children = [0,0,0]
        self.parent = parent
        self.right = right
        self.left = left

    def insert_child(self,value):
      if value > self.value:
        self.right =  binary_tree_node(value,parent=self)
        self.number_of_children[1] +=1
      else:
        self.left = binary_tree_node(value,parent=self)
        self.number_of_children[0] +=1
      self.number_of_children[2]+=1
      return

    def update_child_counter(self):
      if self.right:
        self.number_of_children[1] = self.right.number_of_children[2]+1
      else:
        self.number_of_children[1] = 0
      if self.left:
        self.number_of_children[0] = self.left.number_of_children[2]+1
      else:
        self.number_of_children[0] = 0
      self.number_of_children[2] = self.number_of_children[1]+self.number_of_children[0]
      return
    def unbalanced(self,c):
      if self.number_of_children[0] > c*self.number_of_children[2]:
        return 1
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
  def __init__(self,c,root:binary_tree_node=None) -> None:
      self.root = root
      self.c = c
  def insert(self,value):
      if not self.root:
        self.root = binary_tree_node(value)
        return
      current_node = self.root
      while 1:
        if value > current_node.value:
          if not current_node.right:
            break
          current_node = current_node.right
        else:
          if not current_node.left:
            break
          current_node = current_node.left
      node = binary_tree_node(value,parent=current_node)
      if value > current_node.value:
        current_node.right = node
      else:
        current_node.left = node
      node.update_child_counter()
      while current_node:
        current_node.update_child_counter()
        child = current_node
        current_node = current_node.parent
        
        if child.unbalanced(self.c):
          child = binary_tree.balanced(self.c,child)
        if current_node:
          if child.value > current_node.value:
            current_node.right = child
          else:
            current_node.left = child
          
        else:
          self.root = child
          return
      
  def in_order_walk(self):
    return self.root.in_order_walk()
  def balanced(c,node,return_type = "node"):
        """
            Balances a BST using insertion of a balanced binary search tree
        """
        arr = node.in_order_walk()
        new_root = binary_tree.sorted_array_to_bst(arr)
        tree = binary_tree(c,new_root)
        tree.root.parent = node.parent
        if return_type == "node":
          return tree.root
        return tree

  def sorted_array_to_bst(arr):

        if not arr:
            return None
        mid = (len(arr)) // 2
        root = binary_tree_node(arr[mid])
        root.left= binary_tree.sorted_array_to_bst(
            arr[:mid])
        root.right= binary_tree.sorted_array_to_bst(
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


if __name__ == "__main__":
  tree = binary_tree(0.5)
  data = list(np.random.randint(-100,100,50))
  for el in data:
    tree.insert(el)
  tree.display()