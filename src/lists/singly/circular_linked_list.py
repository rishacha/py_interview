from lists.singly.linked_list import LinkedList


class CircularList(LinkedList):
    def __init__(self, data=None):
        super().__init__(data)

    def append_head(self, data):
        return self.append(data)

    def append_tail(self, data):
        return self.append(data)

    def append(self, data):
        temp = self.head
        while temp.next is not None and temp.next != self.head:
            temp = temp.next
        temp.next = self.Node(data)
        temp = temp.next
        temp.next = self.head
        self.size += 1

    @LinkedList.validate
    @LinkedList.check_empty
    def delete(self, data):
        ptr = None
        temp = self.head

        is_found = False
        while temp.next is not None and temp.next != self.head:
            if temp.data == data:
                is_found = True
                if temp == self.head:
                    last = self.head
                    while last.next is not None and last.next != self.head:
                        last = last.next
                    self.head = temp.next
                    last.next = self.head
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

    @LinkedList.validate
    @LinkedList.check_empty
    def search(self, data):
        """
        Returns True if the data exists in the circular list
        Return False if the data doesn't exist
        """

        temp = self.head
        while temp.next is not None and temp.next != self.head:
            if temp.data == data:
                return True
            temp = temp.next
        if temp.data == data:
            return True
        return False

    def traverse(self):
        temp = self.head
        while temp.next is not None and temp.next != self.head:
            print(temp.data, end="-->")
            temp = temp.next
        print(temp.data, end="-->head-CIRCULAR")
