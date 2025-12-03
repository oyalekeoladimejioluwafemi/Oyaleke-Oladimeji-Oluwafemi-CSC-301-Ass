#                      DATA STRUCTURES PRACTICAL REPORT
#                 QUEUE IMPLEMENTATION USING LINKED NODES
# ==============================================================================
# Student: OYALEKE OLADIMEJI OLUWAFEMI
# Matric No: 230502090
# Course: CSC 301 — Data Structures


class NodeUnit:
    def __init__(self, item):
        self.item = item
        self.link = None


class ChainQueue:
    def __init__(self):
        self.start = None
        self.end = None

    def insert(self, value):
        """Add a value to the back of the queue."""
        fresh = NodeUnit(value)

        if self.end is None:
            self.start = self.end = fresh
            return

        self.end.link = fresh
        self.end = fresh

    def remove(self):
        """Remove element from queue front and return it."""
        if self.start is None:
            raise RuntimeError("Queue is empty.")

        data_out = self.start.item
        self.start = self.start.link

        if self.start is None:
            self.end = None

        return data_out


# Example run
q = ChainQueue()
q.insert(100)
q.insert(200)

print(q.remove())   # Expected: 100
print(q.remove())   # Expected: 200
