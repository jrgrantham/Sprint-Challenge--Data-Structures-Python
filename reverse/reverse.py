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

  # def reverse_list(self):

  #   # store elements to preserve original 'next' once its link is reversed
  #   # start at the head and store current element
  #   current_element = self.head
  #   # initial previous element for the head doesn't exist
  #   prev_element = None
  #   # store the following element before changing the link
  #   next_element = current_element.get_next()

  #   while current_element:
  #     current_element.set_next(prev_element)
  #     current_element = next_element
  #     prev = current_element
  #   self.head = prev


    # a -> b -> c -> d
    
  def reverse_list(self):

      # store the initial element
      current = self.head
      # store the previous element
      previous = None

      # iterate until through list and swap next to previous
      while current:
          # store the 'next' element to preserve it.
          next = current.next_node
          # swap the current elements 'next' to 'previous'
          current.next_node = previous
          # update the 'previous' to current for next iteration
          previous = current
          # update the 'current' to the 'next' for next iteration
          current = next
      # once complete, set the head.
      self.head = previous