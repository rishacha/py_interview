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
                raise Exception("data type cannot be None")
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

    def __init__(self,data=None):
        if data is None:
            # raise Exception("Data cannot be None")
            self.size = 0
            self.root = None
            return
        self.root = self.Node(data)
        self.last = self.root
        self.size = 1

    def traverse(self):
        """
        Prints the list in order
        """
        if self.empty():
            return print("List is empty !")
        return self.root.traverse()

    def append_tail(self,data):
        """
        Add an element to the tail of the list
        """
        if data is None:
            raise Exception("data cannot be None")
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
        if data is None:
            raise Exception("Cannot delete None type data from list")

        if self.empty():
            raise Exception("Cannot delete empty list !")

        ptr = None
        temp = self.root

        is_found = False
        while temp is not None:
            if temp.data == data:
                is_found = True
                if temp == self.root:
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
        if not is_found:
            print(f"{data} not found in List")

    
    def search(self, data):
        """
        Returns True if the data exists in the list
        Return False if the data doesn't exist
        """
        if data is None:
            raise Exception("Cannot search None type data from list")

        temp = self.root
        while temp!=None:
            if temp.data==data:
                return True
            temp = temp.next
        return False
    
    # def reverse(self):
    #     """
    #     #Reverses the list
    #     """
    #     pass

    # def concatenate(self,list2):
    #     pass
    

    def empty(self):
        return True if self.size == 0 else False
            
        

        
        
            
    
        
    