from dll import DoublyLinkedList


class Stack():
    def __init__(self):
        super().__init__()
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        return

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
