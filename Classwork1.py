#                      DATA STRUCTURES PRACTICAL REPORT
#                   STACK IMPLEMENTATION USING PYTHON LIST
# ==============================================================================
# Student: OYALEKE OLADIMEJI OLUWAFEMI
# Matric No: 230502090
# Course: CSC 301 – Data Structures


class StackList:
    def __init__(self):
        self.items = []

    def add(self, element):
        """Push an element onto the stack."""
        self.items.append(element)

    def remove(self):
        """Pop top element if stack is not empty."""
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def top(self):
        """View the element at the top without removing it."""
        if not self.items:
            return None
        return self.items[-1]

    def empty(self):
        """Check if the stack contains no elements."""
        return len(self.items) == 0


# Demonstration
stack = StackList()
stack.add(15)
stack.add(35)

print(stack.remove())   # Expected: 35
print(stack.top())      # Expected: 15
