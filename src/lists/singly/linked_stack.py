from attr import validate
from lists.singly.linked_list import LinkedList


class LinkedStack(LinkedList):
    """
    This class contains an implementation of the Stack class.
    A Stack follows - `LIFO - Last-In-First-Out` policy
    """

    def __init__(self, data=None):
        """
        Initialize top pointer
        """
        super().__init__(data=data)
        self.top = self.head

    @LinkedList.validate
    def push(self, data):
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = self.Node(data)
        self.top = ptr.next
        self.size += 1

    @LinkedList.check_empty
    def pop(self):
        data = self.top.data
        ptr = self.head
        while ptr.next is not None and ptr.next != self.top:
            ptr = ptr.next
        ptr.next = None
        if ptr != self.top:
            self.top = ptr
        else:
            self.top = None
            self.head = None
        self.size -= 1
        return data
