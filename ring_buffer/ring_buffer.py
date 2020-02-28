from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # # if length is at capacity
        # if self.storage.__len__() == self.capacity:
        #     # remove the tail
        #     self.storage.remove_from_head()
        # # add item to head
        # self.storage.add_to_tail(item)

        # check if empty, if so, initialise
        if self.storage.length == 0:
            # create head if no initial entry
            self.storage.add_to_head(item)
            # set current position to location used
            self.current = self.storage.head

        # check if storage is in use but not full
        elif self.storage.length < self.capacity:
            # add item to next position
            self.storage.add_to_tail(item)
            # set current position to location used
            self.current = self.storage.tail

        # if storage is full
        # move storage position to next location
        else:
            # if current is at the tail
            if self.current == self.storage.tail:
                # move position to the head
                self.current = self.storage.head
            else:
                # otherwise move position to next position
                self.current = self.current.next
            # overwrite value in current position
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        # set first node to add to contents
        node = self.storage.head
        # loop over storage and add to contents
        while node:
            # add current value
            list_buffer_contents.append(node.value)
            # move to next value
            node = node.next

        return list_buffer_contents

# buffer = RingBuffer(5)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e') # 5
# buffer.append('f')
# buffer.append('g')
# buffer.append('h')
# buffer.append('i')
# buffer.append('j') # 10
# buffer.append('k')
# buffer.append('l')
# print(buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
