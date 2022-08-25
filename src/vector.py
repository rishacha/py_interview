"""
This class implements a vector in python
"""


class Vector:
    def __init__(self):
        """
        lst: Underlying list
        capacity: Total storage of the vector
        current: Total number of elements currently present in the vector
        """
        self.lst = []
        self._capacity = 0
        self.current = 0

    def size(self):
        """
        Returns the number of items
        """
        return self.current

    def capacity(self):
        """
        Number of items it can hold
        """
        return self._capacity

    def is_empty(self):
        return True if self.current > 0 else False

    def at(self, index):
        """
        Returns item at given index, blows up if index out of bounds
        """
        return self.lst[index]

    def push(self, item):
        """
        Append item at the end of the vector
        """
        self.current = self.current + 1
        if self.current > self._capacity:
            self._capacity = 2 * self._capacity
            # Resize your static list here
        self.lst.append(item)

    def insert(self, index, item):
        """
        Inserts item at index, shifts that index's value and trailing elements to the right
        """
        self.lst.insert(index, item)

    def prepend(self, item):
        """
        Add item at idx 0
        """
        self.lst.insert(0, item)

    def pop(self):
        if self.count > 0:
            return self.lst.pop()

    def delete(self, index):
        del self.lst.insert[index]

    def remove(self, item):
        """
        looks for value and removes index holding it(even if in multiple places)
        """
        pass

    def find(item):
        """
        looks for value and returns first index with that value, -1 if not found
        """
        pass
