from lists.singly.linked_list import LinkedList

class CircularList(LinkedList):
    def __init__(self, data=None):
        super().__init__(data)
    
    def append_head(self, data):
        return self.append(data)
    
    def append_tail(self, data):
        return self.append(data)

    def append(self,data):
        temp = self.root
        while temp.next is not None and temp.next != self.root:
            temp = temp.next
        temp.next = self.Node(data)
        temp = temp.next
        temp.next = self.root
        self.size+=1
    
    def delete(self,data):
        if data is None:
            raise Exception("Cannot delete None type data from circular list")

        if self.empty():
            raise Exception("Cannot delete empty list !")
    
        ptr = None
        temp = self.root

        is_found = False
        while temp.next is not None and temp.next!=self.root:
            if temp.data == data:
                is_found = True
                if temp == self.root:
                    last = self.root
                    while last.next is not None and last.next != self.root:
                        last = last.next
                    self.root = temp.next
                    last.next = self.root
                    self.size -= 1
                    break
                else:
                    ptr.next = temp.next
                    temp = None
                    self.size -= 1
                    break
            ptr = temp
            temp = temp.next
        if not is_found:
            print(f"{data} not found in Circular List")

    def search(self,data):
        """
        Returns True if the data exists in the circular list
        Return False if the data doesn't exist
        """

        if data is None:
            raise Exception("Cannot search None type data from circular list")
        
        if self.empty():
            raise Exception("Cannot search empty list !")

        temp = self.root
        while temp.next is not None and temp.next != self.root:
            if temp.data == data:
                return True
            temp = temp.next
        if temp.data == data:
            return True
        return False
    def traverse(self):
        temp = self.root
        while temp.next is not None and temp.next != self.root:
            print(temp.data, end="-->")
            temp = temp.next
        print(temp.data, end="-->ROOT-CIRCULAR")

