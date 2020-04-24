from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        if self.capacity < 1:
            return

        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head

        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.current.next

        else:
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        item = self.storage.head

        while item is not None:
            list_buffer_contents.append(item.value)
            item = item.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# test = RingBuffer(5)

# test.append('a')
# test.append('b')
# test.append('c')
# test.append('d')
# test.append('e')
# test.append('f')
# # test.append('g')
# # test.append('h')
# # test.append('i')
# # test.append('j')
# # test.append('k')
# test.get()
