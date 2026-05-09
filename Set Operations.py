# Program to perform union, intersection, symmetric difference, and subset operations
def perform_set_operations():
    # User input for two sets
    set_a = set(map(int, input("Enter elements of Set A (space separated): ").split()))
    set_b = set(map(int, input("Enter elements of Set B (space separated): ").split()))

    print(f"\nSet A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union: {set_a | set_b}")
    print(f"Intersection: {set_a & set_b}")
    print(f"Symmetric Difference: {set_a ^ set_b}")
    print(f"Is A a subset of B?: {set_a.issubset(set_b)}")

perform_set_operations()

"""
Expected Output:
Enter elements of Set A: 1 2 3 4
Enter elements of Set B: 3 4 5 6
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Symmetric Difference: {1, 2, 5, 6}
Is A a subset of B?: False
"""