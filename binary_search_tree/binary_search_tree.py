from stack import Stack
from queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if our new nodes value is less than the current nodes value
        if value < self.value:
            # does it have a child to the left?
            if self.left is None:
                # place our new node here
                self.left = BinarySearchTree(value)
                return
            # otherwise
            else:
                # repeat process for the left
                self.left.insert(value)

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
        if value >= self.value:
            # does it have a child to the right?
            if self.right is None:
                # place our new node here
                self.right = BinarySearchTree(value)
                return
            # otherwise
            else:
                # repeat the process for the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the target is the root node, return True
        if self.value == target:
            return True
        # if value is less than root node and left is not None, recurse
        elif target < self.value and self.left:
            return self.left.contains(target)
        # if value is greater than root node and right is not None, recurse
        elif target > self.value and self.right:
            return self.right.contains(target)
        # otherwise
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # maximum value must be on the right
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # From Tom's lecture
        # base case run the callback passing in the selfs value
        cb(self.value)
        # if left exists
        if self.left:
            # run the for each on left
            self.left.for_each(cb)
        # if right exists
        if self.right:
            # run the for each on right
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node != None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        if node == None:
            return
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            node = q.dequeue()
            print(node.value)
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
            return
        s = Stack()
        s.push(node)
        while s.size > 0:
            node = s.pop()
            print(node.value)
            if node.left != None:
                s.push(node.left)
            if node.right != None:
                s.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
