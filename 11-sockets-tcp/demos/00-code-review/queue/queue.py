from node.node import Node


class Queue:
    def __init__(self, iterable=[]):
        self.back = None
        self.front = None
        self._length = 0

        for item in iterable:
            self.enqueue(item)

    def __repr__(self):
        """print out the front of the q"""
        return 'Queue front: {}'.format(self.front.val)

    def __str__(self):
        """print out the back of the q"""
        return 'Queue back: {}'.format(self.back.val)

    def enqueue(self, val):
        node = Node(val)

        if self._length == 0:
            self.front = self.back = node
            self._length += 1
            return node

        # self.back.next = self.back = node

        self.back.next = node
        self.back = node

        self._length += 1
        return node

    def dequeue(self):
        if self._length == 0:
            raise IndexError('List is empty')

        temp = self.front
        self.front = temp.next
        self._length -= 1
        return temp
