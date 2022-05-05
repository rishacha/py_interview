from lists.singly.linked_list import LinkedList

class LinkedQueue(LinkedList):
    """
    Implements a first-in-first-out (FIFO) approach
    """
    def __init__(self, data=None):
        super().__init__(data)

    def enqueue(self, data):
        self.append_tail(data=data)

    def dequeue(self):
        if self.empty():
            raise Exception("Cannot dequeue from empty queue !")
        data = self.root.data
        self.root = self.root.next
        self.size-=1
        return data
    
