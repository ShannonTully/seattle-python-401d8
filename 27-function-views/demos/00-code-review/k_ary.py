class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []


class KTree:
    def __init__(self):
        self.root = None

    def insert_at_all_parent_vals(self, parent_val, val=None):
        node = Node(val)

        if self.root is None:
            self.root = node
            return

        # traverse to find parent(s)
        # insert at parent(s) children
