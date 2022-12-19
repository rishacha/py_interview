"""
This class implements a **SINGLY** linked list
"""


from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def validate(func: F) -> F:
    """
    Validate the data for the node.
    """

    def inner(self: Any, data: Any) -> F:
        if data is None:
            raise Exception("Data type cannot be None")
        return func(self, data)

    return inner


class LinkedList:
    """
    Class contains code for a linked list
    """
    class Node:
        def __init__(self, data) -> None:
            """
            A `node` contains -

            1. Data of the node element
            1. A pointer to the `next` Node
            """
            if data is None:
                raise Exception("Data type cannot be None")
            self.data: Any = data
            self.next: Any = None

        def traverse(self):
            """
            Will test the traversal for this list in the test class
            """
            print(self.data, end="-->")
            if self.next is not None:
                return self.next.traverse()
            return

    def __init__(self, data=None) -> None:
        if data is None:
            # raise Exception("Data cannot be None")
            self.size = 0
            self.head = None
            return
        self.head = self.Node(data)
        self.last = self.head
        self.size = 1

    def empty(self) -> bool:
        return True if self.size == 0 else False

    def check_empty(func):
        def inner(self, *args, **kwargs):
            if self.empty():
                raise Exception("List is empty !!")
            return func(self, *args, **kwargs)

        return inner

    @check_empty
    def traverse(self):
        """
        Prints the list in order
        """
        return self.head.traverse()

    @validate
    def append_tail(self, data):
        """
        Add an element to the tail of the list
        """

        self.last.next = self.Node(data)
        self.last = self.last.next
        self.size += 1

    @validate
    def append_head(self, data):
        """
        Add an element to the head of the list
        """
        temp = self.head
        self.head = self.Node(data)
        self.head.next = temp
        self.size += 1

    @validate
    @check_empty
    def delete(self, data):
        """
        Deletes first occurence of the data in the list
        """
        ptr = None
        temp = self.head

        is_found = False
        while temp is not None:
            if temp.data == data:
                is_found = True
                if temp == self.head:
                    self.head = temp.next
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

    @validate
    @check_empty
    def search(self, data):
        """
        Returns True if the data exists in the list
        Return False if the data doesn't exist
        """
        temp = self.head
        while temp != None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def reverse(self) -> None:
        """
        Reverses the list.

        Write a recursive function for this.
        """
        self.head = self.reverse(self.head.next)


    # def concatenate(self,list2):
    #     pass
