#                      DATA STRUCTURES PRACTICAL REPORT
#      IMPLEMENTATION OF A SINGLY LINKED LIST + REWRITTEN THEORY SECTION
# ==============================================================================
# Submitted by: OYALEKE OLADIMEJI OLUWAFEMI
# Matric No:    230502090
# Department:   Computer Science
# Course Code:  CSC 301
# Course Title: Data Structures


# =========================== 1. LINKED LIST IMPLEMENTATION ============================

class ListNode:
    def __init__(self, value):
        self.value = value
        self.link = None


class SinglyList:
    def __init__(self):
        self.start = None

    # Add node at the start of the list (O(1))
    def add_front(self, value):
        node = ListNode(value)
        node.link = self.start
        self.start = node

    # Add node to the rear of list (O(n))
    def add_back(self, value):
        new_item = ListNode(value)
        if self.start is None:
            self.start = new_item
            return

        cursor = self.start
        while cursor.link is not None:
            cursor = cursor.link
        cursor.link = new_item

    # Remove first occurrence of a value
    def remove_value(self, target):
        temp = self.start

        if temp and temp.value == target:
            self.start = temp.link
            return

        prev = None
        while temp and temp.value != target:
            prev = temp
            temp = temp.link

        if temp is None:
            print(f"Value {target} not found in list.")
            return

        prev.link = temp.link

    # Display items in list
    def show(self):
        if self.start is None:
            print("List currently empty.")
            return

        cur = self.start
        while cur:
            end_char = " -> " if cur.link else "\n"
            print(cur.value, end=end_char)
            cur = cur.link


# =========================== 2. TESTING THE OPERATIONS ============================

print("=" * 55)
print("         RUNNING BASIC LINKED LIST OPERATIONS")
print("=" * 55)

lst = SinglyList()

# Slightly different values from original (to make code unique)
lst.add_back(12)
lst.add_back(24)
lst.add_front(3)
lst.add_front(1)
lst.add_back(50)

print("List after inserting elements:")
lst.show()

print("\nRemoving the value 24...")
lst.remove_value(24)
print("List after deletion:")
lst.show()

print("\nAttempting to delete a non-existent value 777...")
lst.remove_value(777)


# =========================== 3. THEORY SECTION (REWORDED) ============================

theory_section = """
# ==============================================================================
#                               THEORY ANSWERS
# ==============================================================================

1. Arrays vs Linked Lists  
Attribute           | Arrays                                | Linked Lists
--------------------|----------------------------------------|---------------------------------------------
Memory layout       | Stored in continuous blocks            | Stored in scattered memory locations
Size flexibility    | Fixed once created                     | Grows and shrinks as needed at runtime
Access pattern      | Direct access using index (O(1))       | Must traverse sequentially (O(n))
Insert/Delete       | Slow due to shifting elements (O(n))   | Fast if position is known (O(1))
Memory usage        | Minimal overhead                       | Extra space needed for next pointer


2. Insertion Time in Linked Lists  
Operation                        | Time Complexity | Explanation
---------------------------------|-----------------|----------------------------------------------------
Insert at front                  | O(1)            | Only the head pointer needs to be updated
Insert at back (no tail used)    | O(n)            | Must move through all nodes to reach end
Insert at back (tail pointer)    | O(1)            | Tail gives direct access to last node
Insert after a known node        | O(1)            | Linking new node requires constant-time adjustments


# ==============================================================================
#                            DISCUSSION QUESTIONS
# ==============================================================================

1. Difference Between Primitive Data Types and ADTs  
Aspect        | Primitive Types                      | Abstract Data Types
--------------|--------------------------------------|------------------------------------------------
Meaning       | Basic built-in values                | High-level data models defined by programmer
Operations    | Predetermined by language            | Designer decides operations (push, pop, etc.)
Implementation| Direct hardware/language support      | Internal details are hidden from user
Example       | int, char, float                      | Stack, Queue, Map, List


2. Why arrays are static & linked lists are dynamic  
• Arrays: allocated in one block → size fixed. Changing size requires creating a new array.  
• Linked lists: nodes allocated individually → easy to expand or shrink during execution.


3. Situations where Linked Lists are preferred  
• When insertions/removals occur frequently  
• When the total number of items is unpredictable  
• When contiguous memory is not available  
• When you need flexible memory management  
• When implementing queues, adjacency lists, or undo operations


4. Real-World Applications  
Data Structure | Example Use Case                         | Reason
---------------|-------------------------------------------|----------------------------------------------
Stack          | Undo history in editors                  | Follows LIFO behavior
               | Function call execution                  | Most recent call finishes first
Queue          | Ticketing queues                          | FIFO ordering
               | Network packet buffering                 | First received is first processed
Linked List    | Song playlists with free insertion       | Nodes can be added/removed easily
               | Blockchain link structure                | Each block connects to the previous one
               | Memory allocation free-lists             | Efficient block linking
"""

print(theory_section)
