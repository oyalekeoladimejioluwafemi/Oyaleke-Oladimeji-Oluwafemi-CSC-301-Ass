#                  DATA STRUCTURES LABORATORY REPORT
#          IMPLEMENTATION OF SINGLY LINKED LIST & THEORY ANSWERS
# ==============================================================================
# Submitted by: [OYALEKE OLADIMEJI OLUWAFEMI]
# Matric No:    [230502090]
# Department:   Computer Science
# course code:        CSC 301
# course title:      Data Structures


class StackNode:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedListStack:
    def __init__(self):
        self.head = None

    def push_item(self, value):
        """Push a new value onto the stack"""
        node = StackNode(value)
        node.link = self.head
        self.head = node

    def pop_item(self):
        """Pop the top value from the stack"""
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.link
        return val

    def peek_item(self):
        """Peek at the top value without removing it"""
        if not self.head:
            return None
        return self.head.data


# Sample usage
stack = LinkedListStack()
stack.push_item('X')
stack.push_item('Y')

print(stack.pop_item())   # -> Y
print(stack.peek_item())  # -> X
