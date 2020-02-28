class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False
  

  def reverse_list(self):

    # reverse the link and not the order:

    # a -> b -> c -> d
    # a <- b -> c -> d
    # a <- b <- c -> d
    # a <- b <- c <- d

      # store the initial element
      current = self.head
      # store the previous element
      previous = None

      # iterate until through list and swap next to previous
      while current:
          # store the 'next' element to preserve it.
          next_element = current.next_node
          # now swap the current elements 'next' to 'previous'
          current.next_node = previous
          # update the 'previous' to current for next iteration
          previous = current
          # update the 'current' to the 'next' for next iteration
          current = next_element
      # once complete, set the head to the current value
        # the current value gets over written in the loop (step 3)
        # setting the head is stored in 'previous'
      self.head = previous