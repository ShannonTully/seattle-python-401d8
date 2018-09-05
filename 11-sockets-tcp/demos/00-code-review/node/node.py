class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return 'Node value: {}'.format(self.val)

    def __str__(self):
        return self.val
