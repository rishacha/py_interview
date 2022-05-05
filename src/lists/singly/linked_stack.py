from lists.singly.linked_list import LinkedList

class LinkedStack(LinkedList):
    def __init__(self, data=None):
        super().__init__(data=data)
        self.top = self.root

    def push(self, data):
        ptr = self.root
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = self.Node(data)
        self.top = ptr.next
        self.size +=1
    
    def pop(self):
        if self.empty():
            raise Exception("Cannot pop from empty stack !")
        data = self.top.data
        ptr = self.root
        while ptr.next is not None and ptr.next!=self.top:
            ptr = ptr.next
        ptr.next = None
        if ptr != self.top:
            self.top = ptr
        else:
            self.top = None
            self.root = None
        self.size-=1
        return data


    
            
