r"""
This class implements a **DOUBLY** linked list
"""

class DoublyLinkedList():
    def validate(func):
        def inner(self, data):
            if data is None:
                raise Exception("Data type cannot be None")
            return func(self, data)
        return inner

    class BiNode():
        def __init__(self,data):
            self.data = data 
            self.next = None
            self.prev = None
        def traverse_forward(self):
            print(self.data,end="<-->")
            if self.next is not None:
                return self.next.traverse_forward()
            return
        def traverse_backward(self):
            print(self.data,end="<-->")
            if self.prev is not None:
                return self.prev.traverse_backward()
            return
    
    def __init__(self,data=None):
        if data is None:
            self.head = None
            self.size = 0
            self.tail = None
        else:
            self.head = self.BiNode(data)
            self.size=1
            self.tail = self.head
    
    def empty(self):
        return True if self.size == 0 else False
    
    def check_empty(func):
        def inner(self, *args, **kwargs):
            if self.empty():
                raise Exception("List is empty !!")
            return func(self, *args, **kwargs)
        return inner
    @check_empty
    def traverse_forward(self):
        self.head.traverse_forward()
    @check_empty
    def traverse_backward(self):
        self.tail.traverse_backward()
    
    @validate
    def append_head(self, data):
        temp = self.head
        self.head = self.BiNode(data)
        if temp is None and self.size == 0:
            self.tail = self.head
        else:
            self.head.next = temp
            temp.prev = self.head
        self.size+=1
    
    @validate
    def append_tail(self, data):
        temp = self.tail
        self.tail = self.BiNode(data) 
        if temp is None and self.size ==0:
            self.head = self.tail
        else:
            self.tail.prev = temp
            temp.next = self.tail
        self.size +=1
    
    @validate
    @check_empty
    def search(self, data):
        temp = self.root
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False
    
    @validate
    @check_empty
    def delete(self, data):
        temp = self.head
        while temp!= None:
            if temp.data==data:
                self.size-=1
                if temp == self.head and temp == self.tail:
                    self.head = None
                    self.tail = None
                elif temp == self.head:
                    self.head = temp.next
                    self.head.prev = None
                    return
                elif temp == self.tail:
                    self.tail = temp.prev
                    self.tail.next = None
                    return
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp = None
                    return
            temp = temp.next

        
    
