# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # def get_max(self):
    #     maxVal = self.value
    #     rightTree = self.right
    #     while rightTree != None:
    #         if rightTree.value > maxVal:
    #             maxVal = rightTree.value
    #         rightTree = rightTree.right
    #     return maxVal

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        # if not self.left and not self.right:
        #     return cb(self.value)
        # else:
        #     return (self.left.for_each(cb), self.right.for_each(cb))

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # create an empty queue
        queue = Queue()
        # add the starting node to the queue
        queue.enqueue(node)

        # iterate over the queue
        while queue.len() > 0:
            # set the current_node to the first item in the q
            current_node = queue.dequeue()
            # then print the current value
            print(current_node.value)
            # if the current node has a left child
            if current_node.left:
                # call enqueue on the current left
                queue.enqueue(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # call enqueue on the current right
                queue.enqueue(current_node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create an empty stack
        stack = Stack()
        # add the starting node to the stack
        stack.push(node)

        # iterate over the stack
        while stack.len() > 0:
            # set the current_node to the first item in the stack
            current_node = stack.pop()
            # then print the current value
            print(current_node.value)
            # if the current node has a left child
            if current_node.left:
                # call push on the current left
                stack.push(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # call push on the current right
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
