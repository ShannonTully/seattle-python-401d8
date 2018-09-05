from node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        # self._size = 0  (optional)

    # We would also define out magics for more info

    def push(self, val):
        """Doc String"""
        # if type(val) is not int:
        #     raise TypeError('Argument for val must be an Int.')

        try:
            node = Node(val)
        except TypeError:
            # handle the thing
            pass

        node._next = self.top
        self.top = node

        return self.top

    def pop(self):
        pass

    def peek(self):
        pass
