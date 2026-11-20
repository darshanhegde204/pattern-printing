for i in range(0, 5): # Outer loop runs 5 times for rows 0 to 4
    for j in range(0, i + 1):     # Inner loop prints (i + 1) stars so row 0 has 1 star, row 1 has 2, etc.
        print("*", end=" ")
    print()      # Move to the next line after finishing