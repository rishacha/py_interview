from lists.doubly.linked_list import DoublyLinkedList


class DoublyLinkedStack(DoublyLinkedList):
    def __init__(self, data=None):
        super().__init__(data)

    @DoublyLinkedList.validate
    def push(self, data):
        self.append_tail(data)
        self.top = self.tail

    @DoublyLinkedList.check_empty
    def pop(self):
        if self.size == 1:
            data = self.head
            self.head = None
            self.tail = None
            self.size = 0
            self.top = self.tail
            return data

        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        self.top = self.tail
        return temp.data
