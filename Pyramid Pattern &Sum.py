def print_pyramid(rows):
    current_sum = 0
    for i in range(1, rows + 1):
        # Leading spaces
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
            current_sum += j
        print()
    print(f"\nSum of all numbers in pattern: {current_sum}")

print_pyramid(5)

"""
Expected Output:
    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5 
Sum of all numbers in pattern: 35
"""