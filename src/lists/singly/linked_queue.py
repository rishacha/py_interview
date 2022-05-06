from lists.singly.linked_list import LinkedList

class LinkedQueue(LinkedList):
    """
    Implements a first-in-first-out (FIFO) approach
    """
    def __init__(self, data=None):
        super().__init__(data)
    
    @LinkedList.validate
    def enqueue(self, data):
        # TODO Analyze the complexity of this function and improve it if required
        self.append_tail(data=data)
    
    @LinkedList.check_empty
    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        self.size-=1
        return data
    
