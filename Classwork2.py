#                      DATA STRUCTURES PRACTICAL WORK
#                STACK IMPLEMENTATION USING LINKED NODES
# ==============================================================================
# Student: OYALEKE OLADIMEJI OLUWAFEMI
# Matric No: 230502090
# Course: CSC 301 — Data Structures


class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedListStack:
    def __init__(self):
        self.head = None

    def add_item(self, value):
        """Insert a new value at the top of the stack."""
        new_block = StackNode(value)
        new_block.link = self.head
        self.head = new_block

    def remove_item(self):
        """Remove the top element and return its value."""
        if self.head is None:
            return None
        retrieved = self.head.data
        self.head = self.head.link
        return retrieved

    def top_value(self):
        """Look at the element on top without deleting it."""
        if self.head is None:
            return None
        return self.head.data


# Demo run
stack_obj = LinkedListStack()
stack_obj.add_item("X")
stack_obj.add_item("Y")

print(stack_obj.remove_item())   # Expected output: Y
print(stack_obj.top_value())     # Expected output: X
