from src.lists.singly.linked_list import LinkedList
import singly.linked_list


class LinkedStack(LinkedList):
    def __init__(self, data):
        super.__init__(data)
        self.top = self.root

    def push(self, data):
        ptr = self.root
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = self.Node(data)
        self.top = ptr.next
    
            
