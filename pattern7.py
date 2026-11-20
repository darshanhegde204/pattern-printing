sp = 4  # sp used for spacing
for i in range(0, 5):  
    for j in range(0, sp):  # Print leading spaces to center the stars
        print(" ", end=" ")
    for k in range(0, 2 * i + 1):  # Print odd number of stars (1, 3, 5, 7, 9)
        print("*", end=" ")
    sp -= 1  # Decrease leading spaces by 1 
    print()  # Move to the next line after each row