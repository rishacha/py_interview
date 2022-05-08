from lists.doubly.linked_list import DoublyLinkedList

class DoublyLinkedQueue(DoublyLinkedList):
    def __init__(self, data=None):
        super().__init__(data)
    @DoublyLinkedList.validate
    def enqueue(self,data):
        self.append_tail(data)
    @DoublyLinkedList.check_empty
    def dequeue(self):
        if self.size == 1:
            data = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return data

        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        self.size-=1
        return temp.data 