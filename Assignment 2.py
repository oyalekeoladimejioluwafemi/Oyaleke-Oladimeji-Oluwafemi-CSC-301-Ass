#                      DATA STRUCTURES PRACTICAL SOLUTION
#    IMPLEMENTATION OF RECURSION, FIBONACCI, SEARCHING & DYNAMIC ARRAYS
# ==============================================================================
# Name: OYALEKE OLADIMEJI OLUWAFEMI
# Matric No: 230502090
# Department: Computer Science
# Code: CSC 301
# Title: Data Structures Assignment


# ===================== 1) RECURSION: SUM OF FIRST N NUMBERS ======================

def recursive_sum(num):
    if num <= 0:
        return 0
    return num + recursive_sum(num - 1)

print("1) Recursive sum of first 10 natural numbers:")
print(recursive_sum(10))   # Should give 55


# ===================== 2) FIBONACCI SEQUENCE (FIRST 8 TERMS) =====================

def generate_fib(limit):
    sequence = [0, 1]
    for k in range(2, limit):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

print("\n2) Fibonacci sequence (8 terms):")
print(generate_fib(8))
# Example output: [0, 1, 1, 2, 3, 5, 8, 13]


# ===================== 3) INSERTING ELEMENTS INTO A DYNAMIC ARRAY =====================

print("\n3) Adding values into a dynamic Python list:")
dyn_list = []
items = [12, 22, 32, 42, 52]  # slight change to values

for item in items:
    dyn_list.append(item)
    print(f"Added {item} → current list: {dyn_list}")

print("Final list:", dyn_list)


# ===================== 4) LINEAR SEARCH IMPLEMENTATION =========================
