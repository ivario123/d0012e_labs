import numpy as np


class tree_node:
    def __init__(self, key, parent=None, right=None, left=None, sort_method="rotation", sorting_threshold="absolute"):
        self.key = key
        self.parent = parent
        self.right = right
        self.left = left
        self.children_left = 0
        self.children_right = 0
        self.sort_method = sort_method
        self.sorting_threshold = sorting_threshold

    def insert_key(self, key):
        parent = self.search(key)
        if key == parent.key:
            # Recounting nodes
            parent.added_child()
            # If we need to rebalance we will
            parent.needs_balancing()
            print("Duplicate found")
            return
        node = tree_node(key, parent=parent, sort_method=parent.sort_method,
                         sorting_threshold=parent.sorting_threshold)
        if key > parent.key:
            parent.right = node
        else:
            parent.left = node
        # Recounting nodes
        node.added_child()
        # If we need to rebalance we will
        node.needs_balancing()

        node.added_child()
        return

    
    def new_threshold_check(self):
        sum_child = self.children_right+self.children_left
        if self.children_left > c*sum_child:
            return -1
        if self.children_right > c*sum_child:
            return 1
        return 0
    def new_needs_sorting(leaf):
        
        balance = leaf.new_threshold_check()

        if balance != 0:
            leaf.display()
            leaf.balance_rotation()
            leaf.display()
        if leaf.parent==None:
            return leaf


        pass
    def rotate_left(self):
        print("*"*100)
        self.display()
        if self.right == None:
            return
        # Temporary storage variables
        current = {"key":self.key,"parent":self.parent,"right":self.right,"left":self.left,"children_left":self.children_left,"children_right":self.children_right}
        #print(current)
        el = self.right
        right = {"key":el.key,"parent":el.parent,"right":el.right,"left":el.left,"children_left":el.children_left,"children_right":el.children_right}
        el = self.left
        if el:
            left = {"key":el.key,"parent":el.parent,"right":el.right,"left":el.left,"children_left":el.children_left,"children_right":el.children_right}

        rotation_data = {"right_left":self.right.left,"right_children_left":self.right.children_left,"right_children_right":self.right.children_right}
        #print(rotation_data)
        """
                Move the right one up
                Move the top one to the left
                Move the right left to the left
        """
        self.key = right["key"]
        if self.right.right != None:
            self.right.right.parent = self              # Pop from the right side
            self.right = right["right"]               # move the right pointer one index down
        else:
            self.right = None
        # Adding a new left node
        self.left = tree_node(current["key"],parent = self,right = rotation_data["right_left"],left = current["left"],
                                sorting_threshold=self.sorting_threshold,sort_method=self.sort_method)
        if self.left.left:
            self.left.left.parent = self.left
        self.left.children_left= current["children_left"]
        self.left.children_right =  right["children_left"]

        # Shifting the child values
        self.children_left = right["children_left"]+current["children_left"]+1
        self.children_right = right["children_right"]
        if self.parent:
            if self.parent.right == self:
                self.parent.children_right = self.children_left+self.children_right+1
            else:
                self.parent.children_left = self.children_left+self.children_right+1
                
        self.display()
        return


    def rotate_right(self):
        print("*"*100)
        self.display()
        if self.left == None:
            return
        # Temporary storage variables
        current = {"key":self.key,"parent":self.parent,"right":self.right,"left":self.left,"children_left":self.children_left,"children_right":self.children_right}
        #print(current)
        el = self.right
        if el:
            right = {"key":el.key,"parent":el.parent,"right":el.right,"left":el.left,"children_left":el.children_left,"children_right":el.children_right}
        el = self.left
        if el:
            left = {"key":el.key,"parent":el.parent,"right":el.right,"left":el.left,"children_left":el.children_left,"children_right":el.children_right}
        rotation_data = {"left_right":self.left.right,"left_children_right":self.left.children_right,"left_children_left":self.left.children_left}
        #print(rotation_data)
        """
                Move the right one up
                Move the top one to the left
                Move the right left to the left
        """
        self.key = self.left.key
        if self.left.left != None:
            self.left.left.parent = self              # Pop from the left side
            self.left = self.left.left               # move the right pointer one index down
        else:
            self.left = None
        self.right = tree_node(current["key"],parent = self,left = rotation_data["left_right"],right = self.right,
                                sorting_threshold=self.sorting_threshold,sort_method=self.sort_method)
        if self.right.right:
            self.right.right.parent = self.right
        # Log the new child values
        self.right.children_right = current["children_right"]
        self.right.children_left =  left["children_right"]
        self.children_right = current["children_right"]+left["children_right"]+1
        self.children_left = left["children_left"]
        
        if self.parent:
            if self.parent.right == self:
                self.parent.children_right = self.children_left+self.children_right+1
            else:
                self.parent.children_left = self.children_left+self.children_right+1
                
        self.display()
        return

















    

    def needs_balancing(self):
        """Checks if a tree needs to be rebalanced, by using the types sort_method variable.
            I think that this works tho.
        """
        balance = None
        # This should work.
        if self.sort_method == "absolute":
            balance = self.get_balance()
        else:
            sum_children = self.children_right+self.children_left
            if self.children_left and self.children_left > c*sum_children:
                balance = 1
            elif self.children_right and self.children_right > (c)*sum_children:
                balance = -1
            else:
                balance = None

        if balance != None:  
            if self.sort_method == "rotation":
                self.balance_rotation()
            elif self.sort_method == "insert":
                self.balance_insert()
        if self.parent == None:
            return
        else:
            print(f"current node is : {self.key}\nchecking the parent with value : {self.parent.key}")
            self.parent.needs_balancing()
        return 

    def balance_insert(self, start=None, end=None, orderd=None):
        """
            Balance thru insertion of elements in sertain order
        """
        if orderd == None:
            orderd = self.in_order_walk()
            #print(orderd)
            start = 0
            end = len(orderd)-1
        if start > end:
            return self
        #print(orderd[start:end])
        mid = (start+end)//2
        root = tree_node(orderd[mid], parent=self.parent,
                         sort_method=self.sort_method, sorting_threshold=self.sorting_threshold)
        root.left = root.balance_insert(start, mid-1, orderd)
        root.right = root.balance_insert(mid+1, end, orderd)
        return root

    def balance_rotation(self):
        """
            Balance through rotation
            This one might miss a case, don't think so but it seems like it for unbalanced lists. 
            We might have to itterate down the list for very unbalanced lists. So sorting from the base up.
        """
        #main_root.display()
        balancing_factor = self.get_balance()
        if self.sorting_threshold == "absolute":
            if balancing_factor < 2 and balancing_factor > -2:
                return 
        if balancing_factor < -1:
            if self.left != None and not self.left.get_balance() < 0:
                self.left.rotate_left()
            self.rotate_right()
        else:
            if self.right != None and not self.right.get_balance() > 0:
                self.right.rotate_right()
            self.rotate_left()
        #main_root.display()
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
        print(self.key)
        if self.right is not None:
            self.children_right = self.right.children_right + self.right.children_left+1
        else:
            self.children_right = 0
        #self.display()
        if self.parent != None:
            self.parent.added_child()
        return

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
            #line = f"{self.key}"
            if 0:#self.parent:
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
            #s = f"{self.key}"
            if 0:#self.parent:
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
            #s = f"{self.key}"
            if 0: #self.parent:
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
        #s = f"{self.key}"
        if 0:#self.parent:
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


c = .6
counter = 0
"""
      Test section

"""

main_root = None
if __name__ == "__main__":
    nums = list(set(list(np.random.randint(-100, 100, 2*2))))
    main_root = tree_node(nums[0], sorting_threshold="")

    main_root.display()

    for el in nums[1:]:
        if el == 19:
            print("stop")
        main_root.display()
        main_root.insert_key(el)
    main_root.display()
    _sorted = main_root.in_order_walk()
    if sorted(_sorted) == _sorted:
        print("In order walk works")
    else:
        print("In order walk is wack")
    print(_sorted)
    print(sorted(nums))
    print(len(_sorted))
    if _sorted != sorted(nums):
        print("Something went wrong, check log")
    print(main_root.children_left, main_root.children_right,
          c*(main_root.children_right+main_root.children_left))
