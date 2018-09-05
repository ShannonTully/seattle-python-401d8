from node.node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None

        for item in iterable:
            self.push(item)

    def __repr__(self):
        return '<Stack Top: {}>'.format(self.top.val)

    def __str__(self):
        return self.top.val

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        pass

    def peek(self):
        return self.top.val
