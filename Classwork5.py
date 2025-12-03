#                  DATA STRUCTURES LABORATORY REPORT
#          IMPLEMENTATION OF SINGLY LINKED LIST & THEORY ANSWERS
# ==============================================================================
# Submitted by: [OYALEKE OLADIMEJI OLUWAFEMI]
# Matric No:    [230502090]
# Department:   Computer Science
# course code:        CSC 301
# course title:      Data Structures


# Simple Queue using Python list
queue_list = []
queue_list.append(20)   # enqueue
removed_item = queue_list.pop(0)  # dequeue -> O(n) due to shifting
print("Dequeued item:", removed_item)
