"""
This class implements a linked list
"""

class LinkedList():
    class Node():
        def __init__(self,data) -> None:
            """
            A `node` contains - 

            1. Data of the node element
            1. A pointer to the `next` Node 
            """
            if data is None:
                raise Exception("data is None")
            self.data = data
            self.next = None
        def traverse(self):
            """
            Will test the traversal for this list in the test class
            """
            print(self.data, end = "-->")
            if self.next is not None:
                return self.next.traverse()
            return
    def __init__(self,data):
        if data is None:
            raise Exception("Data cannot be None")
        self.root = self.Node(data)
        self.last = self.root
        self.size = 1

    def traverse(self):
        """
        Prints the list in order
        """
        return self.root.traverse()

    def append(self,data):
        """
        Add an element to the tail of the list
        """
        self.last.next = self.Node(data)
        self.last = self.last.next
        self.size +=1
    def append_head(self,data):
        """
        Add an element to the head of the list
        """
        temp = self.root
        self.root = self.Node(data)
        self.root.next = temp
        self.size += 1

    def delete(self,data):
        """
        Deletes first occurence of the data in the list
        """
        ptr = None
        temp = self.root
        while temp is not None:
            if temp.data == data:
                if temp == self.root:
                    if temp.next is None:
                        raise Exception("Cannot delete single element root !")
                    else:
                        self.root = temp.next
                        self.size -= 1
                        break
                else:
                    ptr.next = temp.next
                    temp = None
                    self.size -= 1
                    break
            ptr = temp
            temp = temp.next
    
    def search(self, data):
        """
        Returns True if the data exists in the list
        Return False if the data doesn't exist
        """
        pass

    def reverse(self):
        pass
        
        
            
    
        
    