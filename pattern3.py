for i in range(0, 5): # Outer loop runs 5 times for rows 0 to 4
    for j in range(0, 5 - i):     # Inner loop decreases star count as i increases: 5, 4, 3, 2, 1
        print("*", end=" ")
    print()     # Move to the next line after finishing a row
