#                  DATA STRUCTURES LABORATORY REPORT
#          IMPLEMENTATION OF SINGLY LINKED LIST & THEORY ANSWERS
# ==============================================================================
# Submitted by: [OYALEKE OLADIMEJI OLUWAFEMI]
# Matric No:    [230502090]
# Department:   Computer Science
# course code:        CSC 301
# course title:      Data Structures


class StackArray:
    def __init__(self):
        self.elements = []

    def add(self, value):
        """Push element onto stack"""
        self.elements.append(value)

    def remove(self):
        """Pop element from stack"""
        if not self.elements:
            return None
        return self.elements.pop()

    def top(self):
        """Peek at top element"""
        if not self.elements:
            return None
        return self.elements[-1]

    def empty(self):
        """Check if stack is empty"""
        return len(self.elements) == 0


# Sample usage
stack = StackArray()
stack.add(15)
stack.add(25)

print(stack.remove())  # -> 25
print(stack.top())     # -> 15
